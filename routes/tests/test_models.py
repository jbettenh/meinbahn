from django.test import TestCase
from routes.models import Route


#Django ORM Tests
class RouteModelTest(TestCase):
    def setUp(self):
        Route.objects.create(stop_id=1, direction='North',name='test1')

    def test_route_created(self):
        test_name = Route.objects.get(name='test1')

        self.assertEqual(test_name.stop_id, '1')
    
    def test_passes_correct_route_to_template(self):
        correct_route = Route.objects.filter(name='test1')
        response = self.client.get('/routes/')

        self.assertQuerysetEqual(response.context['route_list'], correct_route)