from django.test import TestCase
from .models import DModel
from django.http import HttpRequest

# Create your tests here.


class DModelTestCase(TestCase):
	def test_setUp(self):
		d_all = DModel.objects.all()
	
	def unique_check(self):
		infile = open('models.py').readlines()
		for n in infile:
			n = n.lstrip(' ')
			if n.startswith('name'):
				if 'unique' and 'True' in n:
					return "Unique Check: Pass"
		return "Unique Check: Failed"
	
	def test_codes(self):
		response = self.client.get('/api/v1/dmodels/')
		self.assertEquals(response.status_code,200)
		
		
		