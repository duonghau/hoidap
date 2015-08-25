from django.conf.urls import url, patterns
from .views import ConversationView, AllConversationView, SendMessageView
urlpatterns=patterns('',
    url(r'^all/$', AllConversationView.as_view(), name="all"),
    url(r'^c/(?P<conversationid>\d+)/$', ConversationView.as_view(), name="view_conversation"),
    url(r'^send/(?P<username>[-\w\d]+)/$', SendMessageView.as_view(), name="send"),
    )