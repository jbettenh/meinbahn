from django.test import TestCase


class DeparturesPageTest(TestCase):
    def test_uses_index_template(self):
        response = self.client.get('/departures/')

        self.assertTemplateUsed(response, 'departures/index.html')
        