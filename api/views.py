import pathlib

from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_queryset = PageVisit.objects.filter(path=request.path)
    my_tittle = "Homepage"
    my_content = {
        "page_title" : my_tittle,
        "page_visit_count" : page_queryset.count(),
        "total_visit_count" : queryset,
    }
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_content)