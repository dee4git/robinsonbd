from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=500, default='service name')
    # serial_number = models.IntegerField(primary_key=True)
    description = models.TextField(max_length=10000, default='description')
    photo = models.ImageField(default='img.png', upload_to='media/services')

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=501, default='service name')
    # serial_number = models.AutoField(primary_key=True)
    description = models.TextField(max_length=10000, default='description')
    photo = models.ImageField(default='img.png', upload_to='media/services')

    def __str__(self):
        return self.name


class QnA(models.Model):
    question = models.CharField(max_length=500, default='question')
    answer = models.CharField(max_length=500, default='answer')

    def __str__(self):
        return self.question


class Stuff(models.Model):
    serial_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=500, default='name')
    designation = models.CharField(max_length=500, default='designation')
    profile_photo = models.ImageField(default='img.png', upload_to='media/profile-photos')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    facebook = models.URLField(max_length=1000, blank=True)
    twitter = models.URLField(max_length=1000, blank=True)
    instagram = models.URLField(max_length=1000, blank=True)
    linked_in = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.serial_number) + ' :: ' + self.designation + ' :: ' + self.name
