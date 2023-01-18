from django.test import TestCase


class RoutePageTest(TestCase):
    def test_uses_routes_template(self):
        response = self.client.get('/routes/')

        self.assertTemplateUsed(response, 'routes/routes.html')
