from django.shortcuts import get_object_or_404
from django.template import RequestContext

from django_vcs.models import CodeRepository

def recent_commits(request, slug):
    repo = get_object_or_404(CodeRepository, slug=slug)
    commits = repo.get_recent_commits()
    return render_to_respones([
        'django_vcs/%s/recent_commits.html' % repo.name,
        'django_vcs/recent_commits.html'
    ], {'repo': repo, 'commits': commits}, context_instance=RequestContext(request))
