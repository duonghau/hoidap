from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from accounts.models import UserProfile
from tag.models import Tag
# Create your models here.

class CommonFields(models.Model):
    content=models.TextField()
    is_active=models.BooleanField(default=True)
    create=models.DateTimeField(auto_now_add=True)
    modify=models.DateTimeField(auto_now=True)
    votes_count=models.IntegerField(default=0)
    downvotes_count=models.IntegerField(default=0)
    rank=models.FloatField(default=0)

    @property
    def content_bref(self):
        return self.content[:100]
    @property
    def content_bref300(self):
        return self.content[:300]
    
    class Meta:
        abstract = True

class Question(CommonFields):
    title=models.CharField(blank=False, max_length=255)
    author=models.ForeignKey(UserProfile, related_name='user_questions')
    tags=models.ManyToManyField(Tag, related_name='tag_questions') 
    slug=models.SlugField(blank=True, max_length=255)
    votes=models.ManyToManyField(UserProfile, related_name='user_question_votes')
    downvotes=models.ManyToManyField(UserProfile, related_name='user_question_downvotes')
    
    def __str__(self):
        return self.title    

    def save(self,*args,**kwargs):
        if not self.pk:
            self.slug=slugify(self.title)
        if self.pk:
            self.votes_count=self.votes.all().count()
            self.downvotes_count=self.downvotes.all().count()
            self.rank=self.votes_count*0.01-self.downvotes_count*0.05
        super(Question,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('question:detail', args=(self.pk, self.slug))

    def get_cname(self):
        return self.__class__.__name__

class Answer(CommonFields):
    author=models.ForeignKey(UserProfile, related_name='user_answers')
    question=models.ForeignKey(Question, related_name='question_answers')
    votes=models.ManyToManyField(UserProfile, related_name='user_answer_votes')
    downvotes=models.ManyToManyField(UserProfile, related_name='user_answer_downvotes')
    
    def __str__(self):
        return self.content[:100]

    def save(self, *args, **kwargs):
        if self.pk:
            self.votes_count=self.votes.all().count()
            self.downvotes_count=self.downvotes.all().count()
            self.rank=self.votes_count*0.01-self.downvotes_count*0.05
        super(Answer,self).save(*args,**kwargs)