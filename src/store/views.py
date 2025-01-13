from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
def add_store(request):
    form = models.storeForm()
    page_title = 'Add Store'
    html_template = 'add-store.html'

    if request.method == 'POST':
        form = models.storeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('store_list'))

    context = {
        'page_title': page_title,
        'form': form
        }
    return render(request, html_template, context)

def store_list(request):
    page_title = 'Store List'
    html_template = 'store-list.html'
    store = models.Store.objects.all()

    context = {
        'page_title': page_title,
        'store': store
        }
    return render(request, html_template, context)