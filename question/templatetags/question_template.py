from datetime import datetime
from django import template
from question.models import Question
register = template.Library()

@register.inclusion_tag('question.html',takes_context=True)
def display_question(context,question):
    args={}
    args['MEDIA_URL']=context['MEDIA_URL']
    args['question']=question
    return args
    
@register.inclusion_tag('answer.html',takes_context=True)
def display_answer(context,answer):
    args={}
    args['MEDIA_URL']=context['MEDIA_URL']
    args['answer']=answer
    return args

@register.inclusion_tag('trending_questions.html')
def trending_questions():
    args={}
    today = datetime.now()
    questions=Question.objects.filter(create__year=today.year,create__month=today.month).order_by('-rank')[:10]
    args['questions']=questions
    return args