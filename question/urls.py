from django.conf.urls import url, patterns
from .views import AddQuestionView, QuestionView, AddAnswerView

urlpatterns=patterns('',
    url(r'^add/$', AddQuestionView.as_view(), name="add"),
    url(r'^(?P<questionid>\d+)-(?P<slug>[-\w\d]+)/$',QuestionView.as_view(), name="detail"),
    )