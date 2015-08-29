from datetime import datetime
from django import template
from tag.models import Tag
register = template.Library()

@register.inclusion_tag('toptags.html')
def toptags():
    tags=Tag.objects.all().order_by('-followers_count')[:5]
    args={}
    args['tags']=tags
    return args

@register.inclusion_tag('trendingtags.html')
def trending_tags():
    today = datetime.now()
    tags=Tag.objects.filter(create__year=today.year,create__month=today.month).order_by('-followers_count')[:5]
    args={}
    args['tags']=tags
    return args

@register.inclusion_tag('mytags.html',takes_context=True)
def mytags(context):
    request=context['request']
    tags=request.user.profile.follow_tags.all()
    args={}
    args['tags']=tags
    return args