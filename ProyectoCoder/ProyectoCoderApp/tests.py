from django.test import TestCase
from django.urls import reverse
from ProyectoCoderApp.models import Repuesto, Vehiculo

# Create your tests here.

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):

        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
    

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
        
    def test_template_name_correct(self):  
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "ProyectoCoderApp/about.html")
        
        