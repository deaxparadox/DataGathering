from django.shortcuts import render

from .models import Site, Data

def home(request):
    sites = Site.objects.all()
    return render(
        request,
        "scrapper/index.html",
        {
            "sites": sites
        }
    )

def pending(request):
    pending = Site.pending.all()
    return render(
        request,
        "scrapper/index.html",
        {
            "sites": pending
        }
    )

def done(request):
    done = Site.done.all()
    return render(
        request,
        "scrapper/index.html",
        {
            "sites": done
        }
    )

def detail(request, id):
    site_detail = Site.objects.get(id=id)
    return render(
        request, 
        "scrapper/details.html",
        {
            "site_detail": site_detail
        }
    )