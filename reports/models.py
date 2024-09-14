from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.utils import timezone

# Incident model
class Incident(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('escalated', 'Escalated'),
        ('resolved', 'Resolved'),
    ]
    INCIDENT_TYPE_CHOICES = [
        ('theft', 'Theft'),
        ('vandalism', 'Vandalism'),
        ('fire', 'Fire'),
        ('accident', 'Accident'),
        ('emergency', 'Emergency'),
        ('medical', 'Medical'),
        ('police', 'Police'),
        ('other', 'Other'),
]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    incident_type = models.CharField(max_length=100, default='default_value')  # Specify a default value
    date_occurred = models.DateTimeField(default=timezone.now)
    date_reported = models.DateTimeField(auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_incidents')

    def __str__(self):
        return self.title

# Community Leader model
class Leader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Community Member model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
