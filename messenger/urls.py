from django.conf.urls import url, patterns
from .views import ConversationView, AllConversationView, SendMessageView,NewConversationView, NewMessageAjaxView
urlpatterns=patterns('',
    url(r'^all/$', AllConversationView.as_view(), name="all"),
    url(r'^t/(?P<username>[-\w\d]+)/$', ConversationView.as_view(), name="view_conversation"),
    url(r'^send/(?P<username>[-\w\d]+)/$', SendMessageView.as_view(), name="send"),
    url(r'^new/$',NewConversationView.as_view(), name="new"),
    url(r'^newajax/(?P<username>[-\w\d]+)/$',NewMessageAjaxView.as_view(), name="newajax"),
    )