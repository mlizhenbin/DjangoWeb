"""DjangoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include
from django.contrib import admin

from DjangoWeb.db import testdb, querydb
from DjangoWeb.getSearch import search_form, search
from DjangoWeb.postSearch import search_post
from DjangoWeb.view import hello

urlpatterns = patterns("",
                       (r'^admin/', include(admin.site.urls)),
                       ('^hello/$', hello),
                       ('^testdb/$', testdb),
                       ('^querydb/$', querydb),
                       ('^searchIndex/$', search_form),
                       ('^search/$', search),
                       ('^search-post/$', search_post),
                       )
