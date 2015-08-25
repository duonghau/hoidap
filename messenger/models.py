from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from accounts.models import UserProfile

# Create your models here.
class Conversation(models.Model):
    participants=models.ManyToManyField(UserProfile, related_name='user_conversations')

    def __str__(self):
        if self.pk:
            return str(self.pk)

class Message(models.Model):
    conversation=models.ForeignKey(Conversation, related_name='conversation_messages')
    sender=models.ForeignKey(UserProfile)
    content=models.TextField()
    create=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:100]

class MessageReadState(models.Model):
    message=models.ForeignKey(Message)
    user=models.ForeignKey(UserProfile, related_name='user_messages_state')
    read_time=models.DateTimeField(null=True)

    def __str__(self):
        return str(self.read_time)

def create_read_state(sender,instance,created,**kwargs):
    if created:        
        for user in instance.conversation.participants.all():
            messagereadstate=MessageReadState()
            messagereadstate.message=instance
            messagereadstate.user=user
            if user == instance.sender:
                messagereadstate.read_time=datetime.now()
            messagereadstate.save()

post_save.connect(create_read_state,sender=Message)