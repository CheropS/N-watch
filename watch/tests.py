from django.test import TestCase
from .models import NeighbourHood

# Create your tests here.
class NeighbourHoodTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sharry=NeighbourHood(name='Muthiga Estate',location='Kinoo', occupants_count='null')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry,NeighbourHood))