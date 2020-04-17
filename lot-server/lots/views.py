#!/usr/bin/env python
#coding:utf-8
import sys,json,re
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from lots.migrations import data_get as data
from lots.migrations import hosts

###伪装工作,强行返回404
def dot_and_look(request,exception):
    return HttpResponse(request,status=404)
def page_not_found(request,exception):
	return HttpResponse(request,status=404)
def server_and_error(request):
	return HttpResponse(request,status=404)
###定义允许访问的Meta头
lock_agent = "PanDownload/2.2.2"
# Client = "net-portable-2.0.0.0"
#锁定开始
def lock(request):
	agent = request.META.get("HTTP_USER_AGENT")
	#lc = request.META.get("HTTP_X_LC_CLIENT_VERSION")
	if agent == lock_agent:
		200
	else:
		return 403

#百度登陆
def logins(request):
    return render(request,"bdlogin.html")

#主要API
def init_api(request):
	code = lock(request)
	# code = 200
	api = request.path
	if code == 403:
		return HttpResponse(request,status=404)
	else:
		if api == "/api/init":
			response= data.init_data()
			return JsonResponse(response)
		elif api == "/api/latest":
			response = data.data_info()
			return JsonResponse(response)
		elif api == "/api/script/list":
			response = data.client_scr()
			return JsonResponse(response)
		else:
			return HttpResponse(request,status=403)