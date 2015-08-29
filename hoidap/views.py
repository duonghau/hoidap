from __future__ import unicode_literals
from itertools import chain
from django.shortcuts import render
from django.views.generic import View
from question.models import Question
from tag.models import Tag

class Index(View):
    def get(self, request):
        args={}
        if request.user.is_authenticated():
            questions=Question.objects.filter(tags__in=request.user.profile.follow_tags.all()).order_by('-create')[:10]
            if questions:
                questions=set(questions)
            # notifications=Notification.objects.filter(recipient=request.user.profile,action='addquestion',is_read=False).order_by('-create')
            # if len(notifications)<10:
            #     notifications=Notification.objects.filter(recipient=request.user.profile,action='addquestion').order_by('-create')[:10]
            # questions=[]
            # for notification in notifications:
            #     if notification.content_object not in questions and notification.content_object.is_active==True:
            #         questions.append(notification.content_object)            
        else:        
            questions=Question.objects.filter(is_active=True).order_by('-create')[:10]
        args['questions']=questions
        return render(request,'index.html', args)

class SearchAjax(View):
    def get(self, request):
        args={}
        term=request.GET.get('term','')
        if term:
            questions=Question.objects.filter(title__icontains=term)[:5]
            tags=Tag.objects.filter(name__icontains=term)[:5]
        objects=chain(questions,tags)
        args['objects']=objects
        return render(request,'search_ajax.html',args)
