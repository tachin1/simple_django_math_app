# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def add(request):
    op1 = request.GET.get('op1')
    op2 = request.GET.get('op2')
    results = float(op1) + float(op2)
    return HttpResponse(results, content_type="text/plain")



def subtract(request):
    op1 = request.GET.get('op1')
    op2 = request.GET.get('op2')
    results = float(op1) - float(op2)
    return HttpResponse(results, content_type="text/plain")


def divide(request):
    op1 = request.GET.get('op1')
    op2 = request.GET.get('op2')
    results = float(op1) / float(op2)
    return HttpResponse(results, content_type="text/plain")


def multiply(request):
    op1 = request.GET.get('op1')
    op2 = request.GET.get('op2')
    results = float(op1) * float(op2)
    return HttpResponse(results, content_type="text/plain")


