from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import Index
urlpatterns = [
    # Examples:
    # url(r'^$', 'hoidap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Index.as_view(), name="index"),
    url(r'^user/',include('accounts.urls', namespace="user")),
    url(r'^tag/', include('tag.urls',namespace="tag")),
    url(r'^question/', include('question.urls',namespace="question"))
]
