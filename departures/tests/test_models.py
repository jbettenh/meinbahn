from django.test import TestCase
from django.utils.timezone import now

from departures.models import Departure


# Django ORM Tests
class DeparturesModelsTest(TestCase):
    def test_saving_and_retrieving(self):
        depart = Departure()
        depart.line = "666"
        depart.destination = "moon"
        depart.next_train_time = now()
        depart.save()

        saved_departure = Departure.objects.first()

        self.assertEqual(saved_departure.line, "666")
        self.assertEqual(saved_departure.destination, "moon")

    def test_departure_repr(self):
        depart = Departure()
        depart.destination = "saturn"
        depart.next_train_time = now()
        depart.save()

        self.assertEqual(repr(depart), "<Departure: saturn>")
