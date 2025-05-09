from django.db import models
import uuid
from django.urls import reverse
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('message', args=[str(self.id)])


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='project', blank=True, null=True)
    image2 = models.ImageField(upload_to='project', blank=True, null=True)
    image3 = models.ImageField(upload_to='project', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])



@receiver(post_delete, sender=Project)
def delete_project_images(sender, instance, **kwargs):
    for field in ['image1', 'image2', 'image3']:
        image = getattr(instance, field)
        if image and os.path.isfile(image.path):
            os.remove(image.path)
