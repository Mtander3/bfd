from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.
class DashBoardHome(LoginRequiredMixin,TemplateView):
	template_name = 'dashboard/dashboard_home.html'
	
	login = '/accounts/login'
	redirect_field_name = 'redirect_to'

	context_object_name = 'user_info'
	context = 'activate'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['user_info'] = self.request.user


		return context 


	

		
	
