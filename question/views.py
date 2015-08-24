import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.generic import View
from .models import Question, Answer
from .forms import AnswerFrom,QuestionForm
from tag.models import Tag
from utils.login_require import LoginRequiredMixin
# Create your views here.

class QuestionView(View):
    def get(self, request, questionid, slug):
        args={}
        try:
            question=Question.objects.get(pk=questionid)
            args['question']=question
            answers=question.question_answers.all().order_by("-create")
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
                tag,created=Tag.objects.get_or_create(name=tagtitle)
                question.tags.add(tag)
                tag.save()
            question.save()
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
                            message['status']='OK'
                            message['message']=""
                            message['votes_count']=currentobject.downvotes_count
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

