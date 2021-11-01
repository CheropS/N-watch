from django.db import models

# Create your models here.

class NeighbourHood(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    occupants_count=models.IntegerField()
    

    def create_neighbourhood(self):
        self.save()

    def save_neighbourhood(self):
        self.save()
    
    def delete_neighbourhood(self):
        self.delete()
    @staticmethod
    def show_all_neighbourhoods():
        return NeighbourHood.objects.all()