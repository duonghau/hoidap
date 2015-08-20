from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.generic import View
from .models import Question, Answer
# Create your views here.

class QuestionView(View):
    def get(self, request, questionid, slug):
        args={}
        try:
            question=Question.objects.get(pk=questionid)
            args['question']=question
            print(question)
        except ObjectDoesNotExist:            
            pass
        return render(request,'question_detail.html',args)

class AddQuestionView(View):

    pass

class AddAnswerView(View):
    pass    

