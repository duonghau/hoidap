from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models import UserProfile

# Create your models here.

class Notification(models.Model):
    sender=models.ForeignKey(UserProfile)
    recipient=models.ForeignKey(UserProfile, related_name='notifications')
    action=models.CharField(blank=True, max_length=10)#vote|downvote, answer,addquestion
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    create=models.DateTimeField(auto_now=True)
    is_read=models.BooleanField(default=False)

    @property
    def notification_string(self):
        string=""
        if self.action=='vote' or self.action=='downvote':
            if self.content_object.__class__.__name__.lower()=='answer':
                string="{} {} your answer: \"{}\"".format(self.sender.fullname, 
                self.action,self.content_object.content[:50])
            elif self.content_object.__class__.__name__.lower()=='question':
                string= "{} {} your question: \"{}\"".format(self.sender.fullname, 
                self.action,self.content_object.title[:50])
        elif self.action=='answer':
            string="{} {} on your question: \"{}\"".format(self.sender.fullname,
                self.action,self.content_object.content[:50])
        elif self.action=="addquestion":
            string="{} add a question:\"{}\"".format(self.sender.fullname, 
                self.content_object.title[:50])
        return string
    @property
    def notification_url(self):
        url=""
        if self.content_object.__class__.__name__.lower()=='answer':
            url=reverse('question:detail', args=(self.content_object.question.pk,
                self.content_object.question.slug))
        elif self.content_object.__class__.__name__.lower()=='question':
            url=reverse('question:detail', args=(self.content_object.pk,self.content_object.slug))                
        return url