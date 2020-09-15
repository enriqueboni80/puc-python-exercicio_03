from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader


def index(request):
    return render(request, "home/index.html")

