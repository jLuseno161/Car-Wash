from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)


class Booking(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, blank=True)
    mobile = models.IntegerField(default=0)
    appointment_date = models.DateTimeField(auto_now_add=True)
    timeframe =(
        ('Morning', 'Morning'),
        ('Evening', 'evening'),
        ('Afternoon', 'afternoon'),)
    
# class Washplan(models.Model):
#     basic = models.ForeignKey(Basic, on_delete)
#     deluxe = 
#     ultimate = 
#     premium = 

class Washplan(models.Model):
    plan = models.CharField(max_length=50)
    price = models.IntegerField(max_length=50)
    duration = models.CharField(max_length=50)
    hwash= models.CharField(max_length=50)
    hdry = models.CharField(max_length=50)
    wshine = models.CharField(max_length=50)
    tdress = models.CharField(max_length=50)
    window = models.CharField(max_length=50)
    sealer = models.CharField(max_length=50)
    vacuum = models.CharField(max_length=50)
    dashboard = models.CharField(max_length=50)
    airfreshner = models.CharField(max_length=50)
    coat = models.CharField(max_length=50)
    vinyl = models.CharField(max_length=50)
    rainx = models.CharField(max_length=50)
