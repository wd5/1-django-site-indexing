from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from index.models import Site, Page

def list(request):
    sites = Site.objects.order_by('-clicks', '-views')
    
    return render_to_response('index/site_list.html', {'sites': sites}, context_instance=RequestContext(request))

def page(request, page_slug):
    page = get_object_or_404(Page, slug=page_slug)
    
    return render_to_response('index/page_page.html', {'page': page}, context_instance=RequestContext(request))

def view(request, site_id):
    s = get_object_or_404(Site, pk=site_id)
    s.views += 1
    s.save()
    
    return render_to_response('index/site_view.html', {'site': s}, context_instance=RequestContext(request))
    
def click(request, site_id):
    s = get_object_or_404(Site, pk=site_id)
    s.clicks += 1
    s.save()
    
    return redirect(s.url)

def stats(request):
    sites = Site.objects.order_by('-clicks', '-views')
    
    return render_to_response('index/site_stats.html', {'sites': sites}, context_instance=RequestContext(request))
