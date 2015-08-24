from django import template
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
