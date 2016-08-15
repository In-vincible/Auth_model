from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import *
from utilities import excel
# Create your vitews here.

def CheckUser(request):
	if request.method == 'POST':
		post = request.POST
		if Auth.objects.filter(username = post['username'], password = post['password']).exists():
			user = Auth.objects.get(username = post['username'] , password = post['password']) 
		else:
			user = None		
		response = {}
		
		if user is not None:
			response['validity'] = True			
			return JsonResponse(response)
		else:
			response['validity'] = False
			return JsonResponse(response)
	return render(request,'test.html')#HttpResponse("Not a valid Reqest !")

def CheckFeatures(request):
	if request.method == 'POST':
		post = request.POST
		level_id = post['level_id']
		feature_id = post['feature_id']
		#feature_relations = levels.objects.filter(level_id = level_id).values_list('level__pk',flat = True)
		level = levels.objects.filter(level_id = level_id)		
		Features = features.objects.filter(levels = level)
		feature = features.objects.get(feature_id = feature_id)
		response = {}
		if feature in Features:
			response['permission'] = True
			return JsonResponse(response)
		else:
			response['permission'] = False
			return JsonResponse(response)
	return render(request,'test.html')#HttpResponse("Not a valid Request !!")
		

			

