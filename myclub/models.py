from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator



class Offer(models.Model):
    offerOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    offerCreatedDate = models.DateTimeField(default=timezone.now)
    offerDescription = models.TextField()
    offerName = models.TextField()
    offerDate = models.DateField(default=timezone.now)
    offerTime = models.TimeField(null=False,default=timezone.now)
    offerDuration = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])    
    offerLocation = models.CharField(max_length=100, blank=True, null=True)
    offerCapacity = models.IntegerField(default=10, validators=[MinValueValidator(3),MaxValueValidator(100)])
    offerIsActive = models.BooleanField(default=True)
    is_taken = models.BooleanField(default=False)
    offerPicture = models.ImageField(upload_to='uploads/offer_pictures/',default='uploads/offer_pictures/default.png', blank=True)
    offerCategory = models.TextField(max_length=100,blank=True)
    

class Event(models.Model):
    eventOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    eventCreatedDate = models.DateTimeField(default=timezone.now)
    eventName = models.TextField()
    eventDescription = models.TextField()
    eventLocation = models.CharField(max_length=100, blank=True, null=True)
    eventDate = models.DateField(default=timezone.now)
    eventTime = models.TimeField(default=timezone.now)
    eventDuration = models.IntegerField(default=1, validators=[MinValueValidator(1),MaxValueValidator(5)])    
    eventCapacity = models.IntegerField(default=10, validators=[MinValueValidator(1),MaxValueValidator(100)])
    eventIsActive = models.BooleanField(default=True)
    eventPicture = models.ImageField(upload_to='uploads/event_pictures/', default='uploads/event_pictures/default.png', blank=True)
    eventCategory = models.TextField(max_length=100,blank=True)

    
class OfferApplication(models.Model):
    applicationDate = models.DateTimeField(default=timezone.now)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    appliedOffer= models.ForeignKey('Offer', on_delete=models.CASCADE)
    isApproved = models.BooleanField(default=False)

class Review(models.Model):
    review = models.TextField()
    createddate = models.DateTimeField(default=timezone.now)
    reviewOffer = models.ForeignKey('Offer', on_delete=models.CASCADE)
    reviewOwner = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',on_delete=models.CASCADE)
    userName = models.CharField(max_length=30, blank=True, null=True)
    userNameSurname = models.CharField(max_length=30, blank=True, null=True)
    userBio = models.TextField(max_length=500, blank=True, null=True)
    userBirthDate = models.DateField(null=True, blank=True)
    userLocation = models.CharField(max_length=100, blank=True, null=True)
    userCredits=models.IntegerField(default=5)
    userReservehour = models.IntegerField(default=0)
    userPicture = models.ImageField(upload_to='uploads/profile_pictures/', default='uploads/profile_pictures/default.png', blank=True)
    userFollowers = models.ManyToManyField(User, blank=True, related_name='userfollowers')
    userCredibility = models.IntegerField(null= True)

#class OfferAttendees(models.Model):

#class EventAttendees(models.Model):

#class Friendship(models.Model)




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
