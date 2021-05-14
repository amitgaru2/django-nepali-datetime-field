from django import forms
from django.core.exceptions import ValidationError

from example_app.models import ExampleModel

from nepali_datetime_field import forms as nepali_datetime_forms


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = '__all__'


class ExampleFilterForm(forms.Form):
    from_date = nepali_datetime_forms.NepaliDateField()
    to_date = nepali_datetime_forms.NepaliDateField()

    def clean(self):
        cleaned_data = super().clean()
        if 'from_date' in cleaned_data and 'to_date' in cleaned_data and cleaned_data['from_date'] > cleaned_data[
            'to_date']:
            raise ValidationError("From date cannot be greater than to date.")
        return cleaned_data
