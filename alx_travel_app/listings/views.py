from django.shortcuts import render
from django.http import JsonResponse

def placeholder(request):
    return JsonResponse({"message": "Listings API is working!"})


# Create your views here.
