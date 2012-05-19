from django import template
from django.core.urlresolvers import resolve, Resolver404
from index.models import Page

register = template.Library()

@register.inclusion_tag('navigation_links.html')
def navigation_links(path):
    try:
        match = resolve(path)
    except Resolver404:
        return {'pages': Page.objects.all()}
    
    if match.url_name == 'index.views.page':
        return {'current_page_slug': match.kwargs['page_slug'], 'pages': Page.objects.all().order_by('order')}
    elif match.url_name == 'index.views.stats':
        return {'current_page_stats': True, 'pages': Page.objects.all().order_by('order')}
    return {'pages': Page.objects.all().order_by('order')}
