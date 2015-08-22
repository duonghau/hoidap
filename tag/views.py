from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.generic import View
from .models import Tag

# Create your views here.
class TagView(View):
    def get(self,request, tagid=None, slug=None):
        args={}
        args.update(csrf(request))
        args['following']=False
        if tagid is not None and slug is not None:
            tag=Tag.objects.get(pk=tagid)
            #get questions
            if tag:
                questions=tag.tag_questions.all().order_by("-create")
                args['questions']=questions
            if request.user.is_authenticated():
                if request.user.profile in tag.tag_followers.all():
                    args['following']=True
            args['tag']=tag
            return render(request, 'tag.html',args)

class TagAllView(View):
    def get(self,request):
        args={}
        tags=Tag.objects.all().order_by('name') 
        args['tags']=tags
        return render(request,'tag_all.html',args)

class AddTagView(View):
    def post(self, request):
        message={}
        if request.user.is_authenticated():
            message['status']="OK"
        else:
            message['status']="False"
            message['message']="You are not login. Please login to continue"

        
