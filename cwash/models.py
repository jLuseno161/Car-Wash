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
    email = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='emails')
    mobile = models.IntegerField()
    appointment_date = models.DateTimeField(auto_now_add=True)
    time_frame = (
        ("Morning", 'Morning'),
        ("Evening", 'Evening'),
        ("Afternoon", 'Afternoon'))
    timeframe = models.CharField(
        choices=time_frame, default=0, blank=False, max_length=50)


# class Washplan(models.Model):
#     basic = models.ForeignKey(Basic, on_delete)
#     deluxe =
#     ultimate =
#     premium =
class services(models.Model):
    service = models.CharField(max_length=50)

    def __str__(self):
        return self.service


class Washplan(models.Model):
    plan = models.CharField(max_length=50)
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    service = models.ManyToManyField(services)

    def __str__(self):
        return self.plan
    # hwash = models.CharField(max_length=50, blank=True, null=True)
    # hdry = models.CharField(max_length=50, blank=True, null=True)
    # wshine = models.CharField(max_length=50, blank=True, null=True)
    # tdress = models.CharField(max_length=50, blank=True, null=True)
    # window = models.CharField(max_length=50, blank=True, null=True)
    # sealer = models.CharField(max_length=50, blank=True, null=True)
    # vacuum = models.CharField(max_length=50, blank=True, null=True)
    # dashboard = models.CharField(max_length=50, blank=True, null=True)
    # airfreshner = models.CharField(max_length=50, blank=True, null=True)
    # coat = models.CharField(max_length=50, blank=True, null=True)
    # vinyl = models.CharField(max_length=50, blank=True, null=True)
    # rainx = models.CharField(max_length=50, blank=True, null=True)
