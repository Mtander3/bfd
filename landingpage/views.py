from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from blog.models import Post
from .forms import ContactForm

#Landing page
def home(request):
	form = ContactForm()
	posts = Post.objects.order_by('-published_date')[:3]
	
	if request.method == "POST":
		form = ContactForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			
			
	return render(request, 'landingpage/index.html',{'posts':posts, 'form':form})
 

