from django.shortcuts import render,redirect,get_object_or_404
from item.models import Item
from .models import Inbox
from .forms import InboxMessageForm
from django.contrib.auth.decorators import login_required


@login_required 
def new_chat(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if item.created_by==request.user:
        return redirect('dashboard:index')
    
    conservations=Inbox.objects.filter(item=item).filter(members__in=[request.user.id])
    if conservations:
        pass

    if request.method == 'POST':
        form=InboxMessageForm(request.POST)

        if form.is_valid():
            conservation=Inbox.objects.create(item=item)
            conservation.members.add(request.user)
            conservation.members.add(item.created_by)
            conservation.save()

            conservation_message=form.save(commit=False)
            conservation_message.conservation=conservation
            conservation_message.created_by=request.user
            conservation_message.save()

            return redirect('item:detail',pk=item_pk)
        
    else:
        form=InboxMessageForm() 
    return render(request,'inbox/new.html',{
        'form':form
    })


@login_required

def inbox(request):
        conservations=Inbox.objects.filter(members__in=[request.user.id])
        return render(request,'inbox/inbox.html',{
             'conservations' : conservations,
        })

@login_required
def detail(request,pk):
        conservation=Inbox.objects.filter(members__in=[request.user.id]).get(pk=pk)

        if request.method == 'POST':
            form=InboxMessageForm(request.POST)
            if form.is_valid():
                conservation_message=form.save(commit=False)
                conservation_message.conservation=conservation
                conservation_message.created_by=request.user
                conservation_message.save()

                conservation.save()
                return redirect('inbox:detail',pk=pk)  
        else:
            form=InboxMessageForm()
    
        return render(request,'inbox/detail.html',{
            'conservation' : conservation,
            'form' : form,
        })

