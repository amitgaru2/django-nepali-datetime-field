import nepali_datetime

from django.db import models
from django.utils.dateparse import date_re
from django.core.exceptions import ValidationError

from . import forms


def parse_date(value):
    """Parse a string and return a nepali_datetime_field.date.

    Raise ValueError if the input is well formatted but not a valid date.
    Return None if the input isn't well formatted.
    """
    match = date_re.match(value)
    if match:
        kw = {k: int(v) for k, v in match.groupdict().items()}
        return nepali_datetime.date(**kw)


class NepaliDateField(models.DateField):
    description = "Nepali Date Field"

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': forms.NepaliDateField,
            **kwargs,
        })

    def from_db_value(self, value, expression, connection):
        return nepali_datetime.date.from_datetime_date(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        value = self.to_python(value)
        if value is not None:
            value = value.to_datetime_date()
        return value

    def to_python(self, value):
        super().to_python()
        if value is None:
            return value

        if isinstance(value, nepali_datetime.date):
            return value

        try:
            parsed = parse_date(value)
            if parsed is not None:
                return parsed

        except ValueError:
            raise ValidationError(
                self.error_messages['invalid_date'],
                code='invalid_date',
                params={'value': value},
            )

        raise ValidationError(
            self.error_messages['invalid'],
            code='invalid',
            params={'value': value},
        )
