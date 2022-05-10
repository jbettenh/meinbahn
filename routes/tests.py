from cgi import test
from urllib import response
from django.test import TestCase
from routes.models import Route


class HomePageRouteTest(TestCase):
    def test_uses_routes_template(self):
        response = self.client.get('/routes/')

        self.assertTemplateUsed(response, 'routes/routes.html')


#Django ORM Tests
class RouteModelTest(TestCase):
    def setUp(self):
        Route.objects.create(name='test1')

    def test_route_created(self):
        test_name = Route.objects.get(name='test1')
        self.assertEqual(test_name.name, 'test1')
        