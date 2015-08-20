from django.conf.urls import url, patterns
from accounts.views import RegisterView, ProfileView, LoginView, LogoutView,RegisterSuccessView,EditProfileView,FollowUser

urlpatterns=patterns('',
    url(r'^register/$',RegisterView.as_view(),name="register"),
    url(r'^registersuccess/$',RegisterSuccessView.as_view(),name="register_success"),
    url(r'^login/$',LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^profile/(?P<username>[-\w\d]+)/$',ProfileView.as_view(),name="profile"),
    url(r'^profile/$',ProfileView.as_view(),name="myprofile"),
    url(r'^changepassword/$',ProfileView.as_view(),name="change_password"),
    url(r'^editprofile/$',EditProfileView.as_view(),name="edit_profile"),
    url(r'^follow/$',FollowUser.as_view())
)