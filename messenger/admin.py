from django.contrib import admin
from .models import Conversation, Message
# Register your models here

admin.site.register(Conversation)

class MessageAdmin(admin.ModelAdmin):
    list_display=('conversation','sender','content','create')
    ordering = ["-create"]

admin.site.register(Message,MessageAdmin)
