from django import template
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter('highlight')
def highlight_filter(text, filename):
    return mark_safe(highlight(
        text,
        guess_lexer_for_filename(filename, text),
        HtmlFormatter()
    ))


@register.simple_tag
def highlight_css():
    return HtmlFormatter().get_style_defs()
