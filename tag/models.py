from time import time
from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.
def get_tags_url(instance, filename):
        return "tags/{}_{}".format(str(time()).replace('.','_'),filename)

class Tag(models.Model):
    name=models.CharField(unique=True, max_length=255,blank=False)
    image=models.ImageField(upload_to=get_tags_url, blank=True)
    description=models.TextField(blank=True)
    questions_count=models.IntegerField(default=0)
    followers_count=models.IntegerField(default=0)
    create=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True)
    
    @property
    def description_bref(self):
        return self.description[:100]
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.slug=slugify(self.name)
        if self.pk:
            self.followers_count=self.tag_followers.all().count()
            self.questions_count=self.tag_questions.all().count()
        super(Tag,self).save(*args,**kwargs)

    def __str__(self):
        return self.name