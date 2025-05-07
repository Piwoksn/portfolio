from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    image1 = models.ImageField(upload_to= 'media', blank=True, null=True)
    image2 = models.ImageField(upload_to= 'media', blank=True, null=True)
    image3 = models.ImageField(upload_to= 'media', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.id)])