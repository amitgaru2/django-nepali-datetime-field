=====================
Nepali DateTime Field
=====================

Highly motivated package from Django's DateField & DateTimeField.

**Note: Currently only supports DateField. DateTimeField will be supported in future releases.**

The package is dependent on `nepali-datetime <https://github.com/dxillar/nepali-datetime>`_ package & the UI for the date picker is forked from https://github.com/leapfrogtechnology/nepali-date-picker.

Installation
------------
::

    $ pip install nepali-datetime-field


Quick start
-----------

1. Add ``nepali-datetime-field`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'nepali-datetime-field',
    ]

2. Import & use ``NepaliDateField`` to your model::

    from nepali_datetime_field.models import NepaliDateField

    class YourModel(models.Model):
        ...
        nepali_date = NepaliDateField()

3. Using the field in your form::
   
    from nepali_datetime_field.forms import NepaliDateField

    class YourForm(forms.Form):
        ...
        nepali_date = NepaliDateField()

4. Whenever using the field in html add the `init` script to load the date picker::
    
    <html>
    {% load static %}
    ...
    <body>
    ...
    </body>
    {% static 'nepali_datetime_field/init.js' %}
    </html>

5. Querying the field::
   
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


Demo
----

Demo of ``example_app`` deployed `here <https://nepali-datetime-field.herokuapp.com/>`__.
