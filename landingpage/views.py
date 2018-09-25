from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post
from . import forms

#Landing page
def home(request):
	posts = Post.objects.order_by('-published_date')[:3]
	return render(request, 'landingpage/index.html',{'posts':posts})
 

def test(request):

	form = forms.ContactForm

	if request.method == "POST":
		form = forms.ContactForm(request.POST)

		if form.is_valid():
			print(form.cleaned_data['name'])
			print(form.cleaned_data['email'])
			print(form.cleaned_data['text'])
	return render(request,'landingpage/test.html',{'form':form})