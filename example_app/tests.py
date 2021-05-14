import nepali_datetime

from django.test import TestCase

from example_app.models import ExampleModel


class ExampleModelTestCase(TestCase):
    def setUp(self):
        ExampleModel.objects.create(nepali_date=nepali_datetime.date(1995, 10, 1))
        ExampleModel.objects.create(nepali_date=nepali_datetime.date(1996, 11, 29))
        ExampleModel.objects.create(nepali_date=nepali_datetime.date(2077, 1, 30))

    def test_nepali_date_query(self):
        # get query
        nepali_date = ExampleModel.objects.get(nepali_date=nepali_datetime.date(1995, 10, 1))
        self.assertEqual(nepali_date.nepali_date.isoformat(), '1995-10-01')

        # filter query
        nepali_dates = ExampleModel.objects.filter(nepali_date=nepali_datetime.date(1996, 11, 29))
        self.assertEqual(nepali_dates.count(), 1)

        # filter range query
        nepali_dates = ExampleModel.objects.filter(
            nepali_date__range=(nepali_datetime.date(1990, 1, 1), nepali_datetime.date(1999, 12, 30)))
        self.assertEqual(nepali_dates.count(), 2)
