from django.conf.urls import url, patterns
from .views import TagView, AddTagView, TagAllView,TagSearchAjaxView
from accounts.views import FollowTag
urlpatterns=patterns('',
    url(r'^all/$', TagAllView.as_view(), name="all"),
    url(r'^addtag/$', AddTagView.as_view(), name="add"),    
    url(r'^(?P<tagid>\d+)-(?P<slug>[-\w\d]+)/$',TagView.as_view(), name="tag_detail"),
    url(r'^follow/$', FollowTag.as_view(),name="follow_tag"),
    url(r'^search/', TagSearchAjaxView.as_view(),name="search"),
    )