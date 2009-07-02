from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from django_vcs.models import CodeRepository

def recent_commits(request, slug):
    repo = get_object_or_404(CodeRepository, slug=slug)
    commits = repo.get_recent_commits()
    return render_to_response([
        'django_vcs/%s/recent_commits.html' % repo.name,
        'django_vcs/recent_commits.html',
    ], {'repo': repo, 'commits': commits}, context_instance=RequestContext(request))

def code_browser(request, slug, path):
    repo = get_object_or_404(CodeRepository, slug=slug)
    context = {'repo': repo}
    file_contents = repo.get_file_contents(path)
    if file is None:
        folder_contents = repo.get_folder_contents(path)
        if folder_contents is None:
            raise Http404
        context['files'], context['folders'] = folder_contents
        return render_to_response([
            'django_vcs/%s/folder_contents.html' % repo.name,
            'django_vcs/folder_contents.html',
        ], context, context_instance=RequestContext(request))
    context['file'] = file_contents
    return render_to_response([
        'django_vcs/%s/file_contents.html' % repo.name,
        'django_vcs/file_contents.html',
    ], context, context_instance=RequestContext(request))

def commit_detail(request, slug, commit_id):
    repo = get_object_or_404(CodeRepository, slug=slug)
    commit = repo.get_commit(commit_id)
    if commit is None:
        raise Http404
    return render_to_response([
        'django_vcs/%s/commit_detail.html' % repo.name,
        'django_vcs/commit_detail.html',
    ], {'repo': repo, 'commit': commit}, context_instance=RequestContext(request))