from django.contrib import admin

from .models import Inbox,InboxMessage
admin.site.register(Inbox)
admin.site.register(InboxMessage)