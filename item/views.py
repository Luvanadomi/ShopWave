from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
from django.contrib.auth.decorators import login_required
import logging
from django.db import IntegrityError

def items(request):
    query=request.GET.get('query','')
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)

    if category_id:
        items=items.filter(category_id = category_id)

    if query:
        items=items.filter(description__icontains=query)
    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id': int(category_id)
    })


def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'item/detail.html',
                  {
                      'item':item,
                      'related_items':related_items,

   
                  })

logger = logging.getLogger(__name__)
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            try:
                item.save()
                return redirect('item:detail', pk=item.id)
            except IntegrityError as e:
                logger.error(f'IntegrityError: {e}')
                form.add_error(None, f'Integrity error: {e}')
        else:
            logger.warning(f'Form is not valid: {form.errors}')
            form.add_error(None, 'Form is not valid.')
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

logger = logging.getLogger(__name__)
@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid(): 
            try:
                form.save()
                return redirect('item:detail', pk=item.id)
            except IntegrityError as e:
                logger.error(f'IntegrityError: {e}')
                form.add_error(None, f'Integrity error: {e}')
        else:
            logger.warning(f'Form is not valid: {form.errors}')
            form.add_error(None, 'Form is not valid.')
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')