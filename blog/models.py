from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import os


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.FileField(blank=True)
    date = models.DateTimeField(
            default=timezone.now)
    
    
    def __str__(self):
        return self.title
    def ext(self):
        name, extension = os.path.splitext(self.photo.name)
        
        if extension == '.jpg':
        	return 'jpg'
        if extension == '.mp4':
        	return 'mp4'
        return 'other'  

    def create(cls,photo, text,date,author, title=''):
    	
    	post= cls(photo, text,date,author, title)
    	return post	
    	