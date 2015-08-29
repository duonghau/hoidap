from django import template
from django.db.models import Q
from messenger.models import Conversation

register = template.Library()

from messenger.models import Message
@register.inclusion_tag('new_message_count.html', takes_context=True)
def message_count(context):
    request=context['request']
    count=Message.objects.filter(recipient=request.user.profile,read=None).count()
    args={}
    args['count']=count
    return args

@register.inclusion_tag('my_conversations.html', takes_context=True)
def my_conversations(context):
    request=context['request']
    profile=request.user.profile
    conversations=Conversation.objects.filter(Q(user_one=profile)|Q(user_two=profile))
    args={}
    args['profile']=profile
    args['conversations']=conversations
    return args