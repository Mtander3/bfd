from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
	
	#blog_id = models.IntegerField(primary_key=True,unique=True)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	title = models.CharField(max_length=200)

	#For landing page blog preview
	short_text = models.CharField(max_length=256)
	text = models.TextField()
	
	created_date = models.DateTimeField(default=timezone.now())
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.pubhlished_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title




