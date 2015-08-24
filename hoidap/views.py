from django.shortcuts import render
from django.views.generic import View
from question.models import Question
class Index(View):
    def get(self, request):
        args={}
        if request.user.is_authenticated():
            questions=Question.objects.filter(is_active=True).order_by('-create')[:10]
        else:        
            questions=Question.objects.filter(is_active=True).order_by('-create')[:10]
        args['questions']=questions
        return render(request,'index.html', args)