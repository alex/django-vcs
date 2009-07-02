from django import template
from django.template.loader import render_to_string

from django_vcs.diff import prepare_udiff

register = template.Library()

@register.filter
def render_diff(text):
    diffs, info = prepare_udiff(text)
    return render_to_string('django_vcs/udiff.html', {'diffs': diffs, 'info': info})
