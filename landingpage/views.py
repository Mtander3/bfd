from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post


#Landing page
def home(request):
	posts = Post.objects.order_by('-published_date')[:3]
	return render(request, 'landingpage/index.html',{'posts':posts})
 

def test(request):

	posts = Post.objects.order_by('-published_date')[:3]
	return render(request,'landingpage/test.html',{'posts':posts})