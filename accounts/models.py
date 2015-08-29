from __future__ import unicode_literals
from time import time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tag.models import Tag
# Create your models here.
def get_profile_url(instance, filename):
    return "profiles/{}_{}".format(str(time()).replace('.','_'),filename)

class UserProfile(models.Model):
    user=models.OneToOneField(User, unique=True, related_name='profile')
    website=models.URLField(max_length=100,blank=True)
    avatar=models.ImageField(upload_to=get_profile_url,blank=True)
    address=models.CharField(blank=True, max_length=255)
    birthday=models.DateField(null=True)
    gender=models.CharField(blank=True, choices=(('Male','Male'),('Female','Female')), max_length=10)
    bio=models.TextField(blank=True)
    rank=models.FloatField(default=0)    
    follows_count=models.IntegerField(default=0)
    followers_count=models.IntegerField(default=0)
    follows=models.ManyToManyField('self', related_name='followers', blank=True, symmetrical=False)
    follow_tags=models.ManyToManyField(Tag, related_name='tag_followers', blank=True)

    @property
    def fullname(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def username(self):
        return self.user.username
        
    @property
    def questions_count(self):
        return self.user_questions.all().count()

    @property
    def answers_count(self):
        return self.user_answers.all().count()

    def __str__(self):
        return self.user.username

    def save(self,*args, **kwargs):
        if self.pk:
            self.follows_count=self.follows.all().count()
            self.followers_count= self.followers.all().count()
        super(UserProfile, self).save(*args, **kwargs)


def create_profile(sender,instance,created,**kwargs):
    if created:
        profile,created=UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_profile,sender=User)
