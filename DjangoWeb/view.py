#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.shortcuts import render


def hello(request):
    list = []
    for i in range(10, 20):
        list.append(i)

    context = {}
    context['hello'] = 'Hello World!'
    context['list'] = list
    return render(request, 'hello.html', context)