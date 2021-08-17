=====================
Nepali DateTime Field
=====================

Highly motivated package from Django's DateField & DateTimeField.

*Note: Currently only supports DateField. DateTimeField will be supported in future releases.*

The package is dependent on `nepali-datetime <https://github.com/dxillar/nepali-datetime>`_ package & the UI for the date picker is forked from https://github.com/leapfrogtechnology/nepali-date-picker.

**Supports: Django 2.0+**

Installation
------------
::

    $ pip install django-nepali-datetime-field


Quick start
-----------

1. Add ``nepali_datetime_field`` to your ``INSTALLED_APPS`` list::

    INSTALLED_APPS = [
        ...
        'nepali_datetime_field',
    ]

2. Importing ``NepaliDateField`` model field to ``models.py`` file::

    from nepali_datetime_field.models import NepaliDateField

    class YourModel(models.Model):
        ...
        nepali_date = NepaliDateField()

3. Importing ``NepaliDateField`` form field to ``forms.py`` file::
   
    from nepali_datetime_field.forms import NepaliDateField

    class YourForm(forms.Form):
        ...
        nepali_date = NepaliDateField()

4. Whenever using ``NepaliDateField`` form field, add the static file by: ``{% static 'nepali_datetime_field/init.js' %}`` in the html template to load the date picker UI::
    
    <html>
    {% load static %}
    ...
    <body>
    ...
    </body>
    {% static 'nepali_datetime_field/init.js' %}
    </html>

5. Querying the model field::
   
    import nepali_datetime

    nepali_date = nepali_datetime.date(1995,10,1)

    # get query
    YourModel.objects.get(nepali_date=nepali_date)

    # filter query
    YourModel.objects.filter(nepali_date=nepali_date)

    # date range query
    from_date = nepali_datetime.date(1990,1,1)
    to_date = nepali_datetime.date(1999,12,30)
    YourModel.objects.filter(nepali_date__range=(from_date, to_date))


More Usage
----------
Check some of the usage details in `example_app/tests.py <https://github.com/dxillar/django-nepali-datetime-field/blob/main/example_app/tests.py>`__.


Demo
----
Demo of the ``example_app`` deployed `here <https://nepali-datetime-field.herokuapp.com/example/create>`__.
