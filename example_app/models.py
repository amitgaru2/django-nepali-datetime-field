from django.db import models

from nepali_datetime_field.models import NepaliDateField


class ExampleModel(models.Model):
    nepali_date = NepaliDateField()

    class Meta:
        ordering = ('-id',)
