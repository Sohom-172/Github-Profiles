from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from .forms import UserRegisterForm,UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import requests
from requests.exceptions import HTTPError	
from datetime import datetime
from .models import Profile

# Create your views here.
'''
def scraped(string):
	try:
		response = requests.get(f'https://api.github.com/users/{request.user.username}')
		#repos_response = requests.get(f'https://api.github.com/users/{request.user.username}/repos')
		response.raise_for_status()
		#repos_response.raise_for_status()
    	# access JSOn content
		jsonResponse = response.json()
		#repos_jsonResponse = repos_response.json()
	return jsonResponse
'''

def index(request):
	if request.user.is_authenticated :
		return render(request,'registration/index.html')
	return render(request,'home.html')

def register(request):
	
	context = {}
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'home.html')
	context['form']=UserRegisterForm()
	return render(request,'registration/reg_form.html',context)
	# attributeError at /register/ --> Profile has no attribute 'USERNAME_FIELD'
	
	'''
	if request.method == 'POST' :
		if request.POST['pass'] == request.POST['passagain']:

			try:
				user = User.objects.get(username=request.POST['uname'])
				return render(request,'register.html',{'error' : "username has already been taken"})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['uname'],password=request.POST['pass'])
				email_arg = request.POST['email']
				fname_arg = request.POST['fname']
				lname_arg = request.POST['lname']
				newProfile = profile(email=email_arg,first_name=fname_arg,last_name=lname_arg,username=user)
				return render(request,'home/html')
		else :

			return render(request,'registration/reg_form.html',{'error':"Passwords don't match"})
	else :
		return render(request,'registration/reg_form.html')
	'''

def update_profile(request):
	if request.user.is_authenticated :
		context = {}
	
		if request.method == "POST":
			form=UserUpdateForm(request.POST,instance=request.user)
			if form.is_valid():
				form.save()
				#logout(request)
				return render(request,'home.html')
		form=UserUpdateForm(request.POST,instance=request.user)
		context['form']=form
		return render(request,'registration/update_form.html',context)
	else :
		return render(request,'home.html')

def explore(request):
	if request.user.is_authenticated :
		User = get_user_model()
		users = User.objects.all()
		usernames=[]
		for person in users:
			usernames.append(person.username)
		context={'dudes':usernames}
		return render(request,'registration/explore.html',context)
	else :
		return render(request,'home.html')

def display(request):
	if request.user.username == request.GET['value'] :
		return render (request,'registration/index.html')
	else :
		context={}
		list_profile = Profile.objects.filter(username__iexact=request.GET['value'])
		user_clicked = list_profile[0]
		required=["github_full_name","first_name","last_name","github_link","github_followers","github_repos","updated_at"]
		#for field in required :
		#	context[field] = user_clicked.field
		
		context["github_ID"] = user_clicked.username
		context["first_name"] = user_clicked.first_name
		context["last_name"] = user_clicked.last_name
		context["github_link"] = user_clicked.github_link
		context["github_followers"] = user_clicked.github_followers
		context["github_repos"] = user_clicked.github_repos
		context["updated_at"] = user_clicked.updated_at


		return render (request,'registration/display.html',context)

	return render(request,'home.html')

def update_now(request):
	if request.user.is_authenticated :
		try:
			response = requests.get(f'https://api.github.com/users/{request.user.username}')
		#repos_response = requests.get(f'https://api.github.com/users/{request.user.username}/repos')
			response.raise_for_status()
		#repos_response.raise_for_status()
    	# access JSOn content
			jsonResponse = response.json()
		#repos_jsonResponse = repos_response.json()
			required=['name','html_url',"followers","repos_url"]
			scraped={}
			for key,value in jsonResponse.items():
				if key in required :
					scraped[key] = value

			request.user.github_link = scraped['html_url']
			request.user.github_full_name = scraped['name']
			request.user.github_followers = scraped["followers"]
			request.user.github_repos = scraped["repos_url"]
			request.user.updated_at = datetime.now()
			request.user.save()
		
		except HTTPError as http_err:
			print(f'HTTP error occurred: {http_err}')
		except Exception as err:
			print(f'Other error occurred: {err}')
		return render(request,'registration/index.html')
	return render(request,'home.html')
