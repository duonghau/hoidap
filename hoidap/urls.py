from django.conf.urls import include, url, patterns
from django.contrib import admin
from .views import Index,SearchAjax
import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'hoidap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Index.as_view(), name="index"),
    url(r'^user/',include('accounts.urls', namespace="user")),
    url(r'^tag/', include('tag.urls',namespace="tag")),
    url(r'^question/', include('question.urls',namespace="question")),
    url(r'^message/', include('messenger.urls', namespace="message")),
    url(r'^notification/', include('notification.urls', namespace="notification")),
    url(r'^search/ajax/$',SearchAjax.as_view(),name="searchajax"),
]
#media files
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

#Change title admin    
admin.site.site_header = "Hoi dap"