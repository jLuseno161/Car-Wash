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


class services(models.Model):
    service = models.CharField(max_length=50)

    def __str__(self):
        return self.service


class Washplan(models.Model):
    plan = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    service = models.ManyToManyField(services, related_name='services', null=True, blank=True)

    def __str__(self):
        return self.plan

class Booking(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='emails')
    mobile = models.IntegerField()
    plan = models.ForeignKey(Washplan, on_delete=models.CASCADE)
    vehicle_choices = (
        ('', 'Choose Vehicle Type'),
        ('Regular Car', 'Regular Car'),
        ('Medium Car', 'Medium Car'),
        ('Compact Suv', 'Compact Suv'),
        ('Mini Van', 'Mini Van'),
        ('Pickup Truck', 'Pickup Truck'),
        ('Cargo Truck', 'Cargo Truck'))

    vehicle_type = models.CharField(
        choices=vehicle_choices, default=0, blank=False, max_length=50)
    appointment_date = models.DateTimeField()
    time_frame = (
        ('', 'Choose Time Frame'),
        ("Morning", 'Morning'),
        ("Evening", 'Evening'),
        ("Afternoon", 'Afternoon'))
    timeframe = models.CharField(
        choices=time_frame, default=0, blank=False, max_length=50)
