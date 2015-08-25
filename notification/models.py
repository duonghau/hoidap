from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from accounts.models import UserProfile

# Create your models here.

class Notification(models.Model):
    sender=models.ForeignKey(UserProfile)
    recipient=models.ForeignKey(UserProfile, related_name='notifications')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    create=models.DateTimeField(auto_now=True)
    is_read=models.BooleanField(default=False)