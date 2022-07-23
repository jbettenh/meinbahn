from django.test import TestCase
from departures.models import Departure
from django.utils.timezone import now

class DeparturesPageTest(TestCase):
    def test_uses_index_template(self):
        response = self.client.get('/departures/')

        self.assertTemplateUsed(response, 'departures/index.html')


# Django ORM Tests
class DeparturesModelsTest(TestCase):
    def test_saving_and_retrieving(self):
        depart = Departure()
        depart.line = '666'
        depart.destination = 'moon'
        depart.next_train_time = now()
        depart.save()

        saved_departure = Departure.objects.first()

        self.assertEqual(saved_departure.line, '666')
        self.assertEqual(saved_departure.destination, 'moon')
