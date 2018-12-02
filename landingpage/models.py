from django.db import models
from django.utils import timezone

from blog.models import Post 
# Create your models here.

class PostView(models.Model):
	model = Post 

class Contact(models.Model):
	name =  models.CharField(max_length=255)
	email =models.EmailField()
	message = models.TextField()
	created_date = models.DateTimeField(default=timezone.now())


