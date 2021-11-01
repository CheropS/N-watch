from django.test import TestCase
from .models import NeighbourHood

# Create your tests here.
class NeighbourHoodTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sharry=NeighbourHood(name='Muthiga Estate',location='Kinoo', occupants_count='1')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharry,NeighbourHood))

    #testing saving method
    def test_save_method(self):
        self.sharry.save_neighbourhood()
        neighbourhoods=NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods)> 0)

    #deleting
    def test_delete_method(self):
        self.sharry.save_neighbourhood()
        self.sharry.delete_neighbourhood()
        neighbourhoods=self.sharry.show_all_neighbourhoods()
        self.assertTrue(len(neighbourhoods) ==0)
    
   
        

