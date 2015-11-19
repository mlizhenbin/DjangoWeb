#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.http import HttpResponse

from DjangoWeb.models import Test

admin.site.register(Test)

def testdb(request):
    test1 = Test(name="w3cschool.cc")
    test1.save()
    return HttpResponse("<p>数据添加成功!</p>")


def querydb(request):
    list = Test.objects.all()
    outs = '';
    for l in list:
        outs += l.name +" "
    return HttpResponse("<p>" + outs + "</p>")
