from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from accounts.models import UserProfile

# Create your models here.
class Conversation(models.Model):
    user_one=models.ForeignKey(UserProfile, related_name='user_ones', null=True)
    user_two=models.ForeignKey(UserProfile, related_name='user_twos', null=True)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.pk:
            return str(self.pk)

class Message(models.Model):
    conversation=models.ForeignKey(Conversation, related_name='conversation_messages')
    sender=models.ForeignKey(UserProfile)
    recipient=models.ForeignKey(UserProfile, related_name='messages')
    content=models.TextField()
    create=models.DateTimeField(auto_now_add=True)
    read=models.DateTimeField(null=True)

    def __str__(self):
        return self.content[:100]
    @property
    def message_bref(self):
        return self.content[:50]