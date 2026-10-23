import nh3
from django import template
from django.utils.safestring import mark_safe
from markdown import markdown

register = template.Library()

ALLOWED_TAGS = {
    'a', 'blockquote', 'br', 'code', 'em', 'h2', 'h3', 'h4', 'hr',
    'li', 'ol', 'p', 'pre', 'strong', 'ul',
}


@register.filter
def article_markdown(value):
    rendered = markdown(value or '', extensions=['sane_lists'])
    cleaned = nh3.clean(
        rendered,
        tags=ALLOWED_TAGS,
        attributes={'a': {'href', 'title'}},
        url_schemes={'http', 'https', 'mailto'},
    )
    return mark_safe(cleaned)