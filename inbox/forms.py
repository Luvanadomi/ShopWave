from django import forms
from .models import InboxMessage

class InboxMessageForm(forms.ModelForm):
    class Meta:
        model=InboxMessage
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={
                'content':'w-full py-4 px-6 border'     
            })
        }