#!/usr/bin/env python
#coding:utf-8
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
	url(r"^bdlogin.html",views.logins),
	url(r"^api",views.init_api)
]

handler403 = views.dot_and_look
handler404 = views.page_not_found
handler500 = views.server_and_error