import nepali_datetime

from django import forms
from django.core.exceptions import ValidationError


class NepaliDateInput(forms.DateInput):
    input_type = 'nepali-date'
    template_name = 'nepali_datetime_field/forms/widgets/nepali_date.html'

    class Media:
        css = {
            'all': ('https://unpkg.com/nepali-date-picker@2.0.2/dist/nepaliDatePicker.min.css',)
        }
        js = (
            'https://code.jquery.com/jquery-3.5.1.slim.min.js',
            'https://unpkg.com/nepali-date-picker@2.0.2/dist/nepaliDatePicker.min.js',
            'nepali_datetime_field/init.js',
        )

    def get_context(self, name, value, attrs):
        if isinstance(value, str):
            try:
                year, month, day = (int(i) for i in value.split('-'))
                nepali_datetime.date(year, month, day)
            except (ValueError, TypeError):
                value = None
        return super().get_context(name, value, attrs)


class NepaliDateField(forms.DateField):
    widget = NepaliDateInput

    def to_python(self, value):
        if value in self.empty_values:
            return None
        try:
            year, month, day = (int(i) for i in value.split('-'))
            nepali_date = nepali_datetime.date(year, month, day)
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return nepali_date
