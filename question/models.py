
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
    slug=models.SlugField(blank=True)
    # votes=models.ManyToManyField(UserProfile, related_name='user_question_votes')
    # downvotes=models.ManyToManyField(UserProfile, related_name='user_question_downvotes')
    
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.pk:
            self.slug=slugify(self.title)
        super(Question,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('question:detail', args=(self.pk, self.slug))

class Answer(CommonFields):
    author=models.ForeignKey(UserProfile, related_name='user_answers')
    question=models.ForeignKey(Question, related_name='question_answers')
    # votes=models.ManyToManyField(UserProfile, related_name='user_answer_votes')
    # downvotes=models.ManyToManyField(UserProfile, related_name='user_answer_downvotes')
    
    def __str__(self):
        return self.content[:100]