from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from utils import oauth2, identity
from utils.models import Scope
from django.shortcuts import render_to_response, redirect
import formwidget
from django.template import RequestContext

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

@login_required
def form(request):
	#TODO add wrapper function for gettting authorizations
	auth = oauth2.getToken(request.user, scope=Scope.objects.get(scope='connector_questionnaire.input_form_data'))
	if auth == None:
		#show user site to authorize the form
		return render_to_response('start_auth.html', {}, context_instance=RequestContext(request))
	return render_to_response('form.html', {}, context_instance=RequestContext(request))

@login_required
def login(request):
	getAttributes(request.user, ['email', 'first_name'])
	return redirect('home')

def logout_success(request):
	return render_to_response('logout_success.html', {}, context_instance=RequestContext(request))

def openid_failed(request):
	return render_to_response('openid_failed.html', {}, context_instance=RequestContext(request))