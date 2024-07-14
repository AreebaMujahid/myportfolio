from django.db import models

# Create your models here.
# models.py



class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Optional description field
    github_link = models.URLField(blank=True)  # Optional GitHub link
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
