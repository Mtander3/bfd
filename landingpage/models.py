from django.db import models
from blog.models import Post 
# Create your models here.

class PostView(models.Model):
	model = Post 