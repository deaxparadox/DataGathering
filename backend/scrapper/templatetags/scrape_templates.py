from django import template 

from ..models import Site

register = template.Library()

@register.inclusion_tag("scrapper/section/latest.html")
def latest(num: int = 5):
    sites = Site.objects.all().order_by("-created")
    if len(sites) > 5:
        sites = sites[:5]
    return {
        "sites": sites
    }
