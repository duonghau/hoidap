from django import template
from tag.models import Tag
register = template.Library()

@register.inclusion_tag('toptags.html')
def toptags():
    tags=Tag.objects.all().order_by('-followers_count')[:10]
    args={}
    args['tags']=tags
    return args

@register.inclusion_tag('mytags.html',takes_context=True)
def mytags(context):
    request=context['request']
    print(request.user)
    tags=request.user.profile.follow_tags.all()
    args={}
    args['tags']=tags
    return args