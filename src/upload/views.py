from django.shortcuts import render
from django.contrib import messages
from . import models
from store.models import Store
from django.conf import settings
import os, csv
# Create your views here.

def upload_csv(request):
    html_template = 'csv-result.html'
    page_title = 'Upload CSV'
    if request.method == 'POST':
        stores = []
        form = models.uploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, 'csv_files', csv_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)
            
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    code, brand, state, name = row
                    stores.append({'code': str(code), 'brand': str(brand), 'state': str(state), 'name': str(name)})
                    Store.objects.create(code=code, name=name, state=state, brand=brand)

            msg = messages.success(request, 'File uploaded and data saved successfully!')
            context = {
                'page_title': page_title,
                'form': form,
                'stores': stores,
                'total': len(stores),
                'msg':msg
            }
            return render(request, html_template, context)
    
    else:
        form = models.uploadCSVForm()
        context = {
            'form': form,
            'page_title': page_title
        }
        return render(request, 'upload-csv.html', context)