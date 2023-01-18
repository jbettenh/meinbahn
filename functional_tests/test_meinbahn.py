from django.test import TestCase
from unittest import skip
from meinbahn import __version__
from routes.models import Route



def test_version():
    assert __version__ == '0.1.0'


class HomePageTest(TestCase):

    def test_uses_home_departures_template(self):
        Route.objects.create(name='home', stop_id='20018107', direction='RBG:71707: :H')

        response = self.client.get('/departures/home/')

        self.assertTemplateUsed(response, 'departures/departures.html')
    
    def test_uses_work_departures_template(self):
        Route.objects.create(name='work', stop_id='20018107', direction='RBG:71707: :R')

        response = self.client.get('/departures/work/')

        self.assertTemplateUsed(response, 'departures/departures.html')

    @skip
    def test_uses_airport_departures_template(self):
        Route.objects.create(name='ariport', stop_id='20018249', direction="'RBG:70072: :R','RBG:70071: :R','DDB:92E11: :R'")

        response = self.client.get('/departures/airport/')

        self.assertTemplateUsed(response, 'departures/departures.html')
