"""
URL configuration for arvhome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from store.views import add_store, store_list, add_state
from upload.views import add_store_csv
from django.conf import settings

ON_CODESPACE = settings.ON_CODESPACE

urlpatterns = [
    path('admin/', admin.site.urls),
    # application path is below
    path('', views.index_view, name='index'),
    path('add-store/', add_store, name='add_store'),
    path('add-store/upload-csv/', add_store_csv, name='add_store_csv'),
    path('add-state/', add_state, name='add_state'),
    path('stores/', store_list, name='store_list'),
]

if ON_CODESPACE:
    urlpatterns += [
        path('__reload__/', include("django_browser_reload.urls")),
    ]
