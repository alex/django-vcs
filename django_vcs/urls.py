from django.conf.urls.defaults import *

urlpatterns = patterns('django_vcs.views',
    url('^(?P<slug>[\w-]+)/$', 'recent_commits', name='recent_commits'),
    url('^(?P<slug>[\w-]+)/browser/(?P<path>.*)$', 'code_browser', name='code_browser'),
    url('^(?P<slug>[\w-]+)/(?P<commit_id>.*)/$', 'commit_detail', name='commit_detail'),
)
