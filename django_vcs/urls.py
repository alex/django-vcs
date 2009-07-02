from django.conf.urls.defaults import *

urlpatterns = patterns('django_vcs.views',
    url('^(?P<slug>[\w-]+)/$', 'recent_commits', name='recent_commits'),
)
