import pathlib

from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_queryset = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_queryset.count()*100.0) / queryset.count()
    except:
        percent = 0
    my_tittle = "Homepage"
    my_content = {
        "page_title" : my_tittle,
        "page_visit_count" : page_queryset.count(),
        "percent" : percent,
        "total_visit_count" : queryset,
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_content)