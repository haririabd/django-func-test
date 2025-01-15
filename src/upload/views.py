from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from . import models
from store.models import Store
from django.conf import settings
import csv
from .csv_upload import upload_file
# Create your views here.

def add_store_csv(request):
    if request.method == 'POST':
        form = models.uploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = upload_file(csv_file)  # Call the upload_file function
            
            with open(file_path, 'r') as f:
                stores = []
                reader = csv.reader(f)
                next(reader)  # Skip the header row
                for row in reader:
                    code, state = row
                    stores.append({'code': str(code), 'state': str(state)})

            m = messages.success(request, 'File uploaded successfully!')
            context = {
                'stores': stores
            }
            return render(request, 'store-list.html', context)
        else:
            form = models.uploadCSVForm()
            context = {
                'form': form
            }
            return(request, context)
    
    else:
        form = models.uploadCSVForm()
        context = {
            'form': form,
        }
        return render(request, 'upload-csv.html', context)