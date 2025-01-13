import pathlib
from django.shortcuts import render

this_dir = pathlib.Path(__file__).resolve().parent

def index_view(request, *args, **kwargs):
    page_title = 'Homepage'
    html_template = 'index.html'

    context = {
        "page_title": page_title,
    }
    return render(request, html_template, context)