from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

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

    # def update_neighbourhood_name(self, value):
    #     self.name = value
    #     self.save_neighbourhood()

    # def update_occupants_count(self, value):
    #     self.occupants_count=value
    #     self.save_neighbourhood()

class User(models.Model):
    name=models.CharField(max_length=40)
    user_id=models.IntegerField()
    neighbourhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    email=models.EmailField()

    def save_profile(self):
        self.save()

    def __str__(self):
        return f'{self.user.username} User'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Business(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField()
    uname=models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_id=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    email=models.EmailField()