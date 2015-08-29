from django.conf.urls import url, patterns
from .views import NewNotificationsView, AllNotificationsView,ViewNotificationView,MarkAllReadView
urlpatterns=patterns('',
    url(r'^new/$',NewNotificationsView.as_view(), name="new"),
    url(r'^all/$',AllNotificationsView.as_view(), name="all"),
    url(r'^view/(?P<notificationid>\d+)/$', ViewNotificationView.as_view(),name="view"),
    url(r'^markallread/$', MarkAllReadView.as_view(), name="allread"),
    )