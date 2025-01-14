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
               'class': "form-control"
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
                'class': "form-control"
            }),
            'state': forms.Select(attrs={
                'class': "form-control"
            })
        }