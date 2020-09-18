from django.contrib.auth.models import User, Group
from django.db import models
# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class OrgnizationalInformation(TimeStamp):
    name = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="organization")
    address = models.CharField(max_length=500)
    slogan = models.CharField(max_length=500, null=True, blank=True)
    contact_no = models.CharField(max_length=500)
    alt_contact_no = models.CharField(max_length=500, null=True, blank=True)
    map_location = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True)
    about_us = models.TextField()
    privacy_policy = models.TextField(null=True, blank=True)
    show_popup = models.BooleanField(default=False)
    popup_image = models.ImageField(
        upload_to="organization", null=True, blank=True)
    facebook = models.CharField(max_length=500)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    youtube = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    featured_photo = models.ImageField(upload_to="organization")
    featured_video_link = models.CharField(max_length=500)
    messenger_script = models.TextField(null=True, blank=True)
    google_analytics_script = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Admin(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=500)
    contact_no = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(
        upload_to='team/admin/', blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        group, group_created = Group.objects.get_or_create(name="Admin")
        self.user.groups.add(group)
        super().save(*args, **kwargs)


class Services(TimeStamp):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Team(TimeStamp):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team')
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(TimeStamp):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField()

    def __str__(self):
        return self.name
