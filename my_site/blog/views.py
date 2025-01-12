from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def starting_page(request):
  return HttpResponse("This is the starting page")


def posts(request):
  pass


def post_detail(request):
  pass
