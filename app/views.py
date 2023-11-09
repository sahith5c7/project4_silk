from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def silk(request):
    return HttpResponse("<h1>WE ARE NOT TALKING ABOUT DIARYMILK SILK</h1>")