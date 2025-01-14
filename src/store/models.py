from django.db import models
from django import forms

# Create your models here.
class State(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name.capitalize()

class stateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']
        widgets = {
           'name': forms.TextInput(attrs={
               'class': "form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
           })
        }
    
class Store(models.Model):
    code = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.code
    
class storeForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['code', 'state']
        widgets = {
            'code': forms.TextInput(attrs={
                'class': "form-control block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            }),
            'state': forms.Select(attrs={
                'class': "form-control block py-2.5 px-0 w-full text-sm text-gray-500 bg-transparent border-0 border-b-2 border-gray-200 appearance-none dark:text-gray-400 dark:border-gray-700 focus:outline-none focus:ring-0 focus:border-gray-200 peer"
            })
        }