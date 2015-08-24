from django import template
from accounts.models import UserProfile
register = template.Library()
@register.inclusion_tag('list_users.html',takes_context=True)
def list_users(context, profiles):
    request = context['request']
    media_url=context['MEDIA_URL']
    user=request.user
    args={}
    args['profiles']=profiles
    args['user']=user
    args['MEDIA_URL']=media_url
    return args

@register.inclusion_tag('top_users.html')
def top_users():
    profiles=UserProfile.objects.all().order_by('-rank')[:10]
    args={}
    args['profiles']=profiles
    return args
