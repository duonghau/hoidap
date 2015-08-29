from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from .models import Question, Answer
from .forms import AnswerFrom,QuestionForm
from tag.models import Tag
from notification.models import Notification
from utils.login_require import LoginRequiredMixin
# Create your views here.

class QuestionView(View):
    def get(self, request, questionid, slug):
        args={}
        try:
            question=Question.objects.get(pk=questionid)
            args['question']=question
            answers=question.question_answers.all().order_by("-rank")
            args['answers']=answers
            if request.user.is_authenticated():                
                answerform=AnswerFrom()
                args['answerform']=answerform
            args.update(csrf(request))
        except ObjectDoesNotExist:            
            pass
        return render(request,'question_detail.html',args)

class AddQuestionView(LoginRequiredMixin,View):
    def get(self,request):
        args={}
        args.update(csrf(request))
        return render(request, 'question_add.html', args)
    
    def post(self,request):
        form=QuestionForm(data=request.POST)
        if form.is_valid():
            question=Question(title=form.cleaned_data['title'],content=form.cleaned_data['content'])
            question.author=request.user.profile
            question.save()
            for tagtitle in form.cleaned_data['tags']:
                try:
                    tag=Tag.objects.get(name=tagtitle)
                except ObjectDoesNotExist:
                    tag=Tag()
                    tag.name=tagtitle
                    tag.save()
                question.tags.add(tag)
                tag.save()
            question.author.rank+=0.01
            question.save()
            question.author.save()
            #notification
            users_notification=[]
            for tag in question.tags.all():
                if tag.tag_followers.all().count() > 0:
                    for profile in tag.tag_followers.all():
                        if profile!=request.user.profile and profile not in users_notification:
                            #create notification
                            notification=Notification()
                            notification.sender=request.user.profile
                            notification.recipient=profile
                            notification.action='addquestion'
                            notification.content_object=question
                            notification.save()
                            users_notification.append(profile)
            for follower in request.user.profile.followers.all():
                if follower not in users_notification:
                    notification=Notification()
                    notification.sender=request.user.profile
                    notification.recipient=follower
                    notification.action='addquestion'
                    notification.content_object=question
                    notification.save()
            return HttpResponseRedirect(reverse('question:detail',args=(question.pk, question.slug)))
        else:
            args={}
            args['form']=form
            args.update(csrf(request))
            return render(request,'question_add.html',args)

class AddAnswerView(LoginRequiredMixin,View):
    def post(self,request,questionid=None, slug=None):
        if questionid:
            form=AnswerFrom(data=request.POST)
            if form.is_valid():                
                try:
                    question=Question.objects.get(pk=questionid)
                    answer=Answer(content=form.cleaned_data['content'], question=question, author=request.user.profile)
                    answer.save()
                    answer.author.rank+=0.01
                    answer.author.save()
                    #notification
                    if question.author!=request.user.profile:
                        notification=Notification()
                        notification.sender=request.user.profile
                        notification.recipient=question.author
                        notification.action="answer"
                        notification.content_object=answer
                        notification.save()
                except ObjectDoesNotExist:
                    pass
        return HttpResponseRedirect(reverse('question:detail',args=(questionid, slug)))

class VoteView(View):
    def post(self, request):
        message={}
        if request.user.is_authenticated():
            objectid=request.POST.get('objectid','')
            objecttype=request.POST.get('objecttype','')
            votetype=request.POST.get('votetype','')
            if objectid and objecttype and votetype:
                if objecttype=='question':
                    currentobject=Question.objects.get(pk=objectid);
                elif objecttype=='answer':
                    currentobject=Answer.objects.get(pk=objectid);
                if currentobject:
                    if votetype=="vote":
                        if request.user.profile in currentobject.votes.all():
                            message['status']='False'
                            message['message']="You can vote only one time"
                        else:
                            currentobject.votes.add(request.user.profile)
                            currentobject.save()
                            currentobject.author.rank+=0.01
                            currentobject.author.save()
                            message['status']='OK'
                            message['message']=""
                            message['votes_count']=currentobject.votes_count
                    elif votetype=="downvote":
                        if request.user.profile in currentobject.downvotes.all():
                            message['status']='False'
                            message['message']="You can downvote only one time"
                        else:
                            currentobject.downvotes.add(request.user.profile)                            
                            currentobject.save()
                            currentobject.author.rank-=0.05
                            currentobject.author.save()
                            message['status']='OK'
                            message['message']=""
                            message['votes_count']=currentobject.downvotes_count
                    #notification
                    if currentobject.author!=request.user.profile:
                        notification=Notification()
                        notification.action=votetype
                        notification.sender=request.user.profile
                        notification.recipient=currentobject.author
                        notification.content_object=currentobject
                        notification.save()
                else:
                    message['status']='False'
                    message['message']="{} isn't exist".format(objecttype)
            else:
                message['status']='False'
                message['message']='Informations is incorrect'
        else:
            message['status']='False'
            message['message']='You must login for this action'
        return HttpResponse(json.dumps(message), content_type = "application/json")

