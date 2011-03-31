from django.test.client import Client
from django.test import TestCase
 
class SimpleTest(TestCase):
    
    #fixtures = ['test_data.json', ]
 
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
 
    def test_home(self):
        '''Test if the homepage renders.'''
        c = Client()
        response = c.get('/')
        self.failUnlessEqual(response.status_code, 200)
