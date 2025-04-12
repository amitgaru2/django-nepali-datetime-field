from django import forms
from django.contrib import admin

from nepali_datetime_field.forms import NepaliDateField

from example_app.models import ExampleModel


class ExampleModelForm(forms.ModelForm):
    nepali_date = NepaliDateField()

    class Meta:
        model = ExampleModel
        fields = '__all__'



# Register your models here.
@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    form = ExampleModelForm
