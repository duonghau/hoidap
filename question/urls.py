from django.conf.urls import url, patterns
from .views import AddQuestionView, QuestionView, AddAnswerView, VoteView

urlpatterns=patterns('',
    url(r'^add/$', AddQuestionView.as_view(), name="add"),
    url(r'^(?P<questionid>\d+)-(?P<slug>[-\w\d]+)/$',QuestionView.as_view(), name="detail"),
    url(r'^(?P<questionid>\d+)-(?P<slug>[-\w\d]+)/answer/$',AddAnswerView.as_view(), name="answer"),
    url(r'^vote/$', VoteView.as_view(), name="vote"),
    )