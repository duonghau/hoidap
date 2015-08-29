from django import template
register = template.Library()
from notification.models import Notification
@register.inclusion_tag('new_notification_count.html', takes_context=True)
def notification_count(context):
    request=context['request']
    count=Notification.objects.filter(recipient=request.user.profile,is_read=False).count()
    args={}
    args['count']=count
    return args