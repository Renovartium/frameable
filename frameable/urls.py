from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.index', name='index'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
)
