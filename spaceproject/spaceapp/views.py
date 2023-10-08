from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def more(request):
    return render(request, 'more.html')
def data(request):
    return render(request, 'data.html')
def explore(request):
    return render(request, 'source.html')
def debris(request):
    return render(request, 'spacedebris.html')
def weather(request):
    return render(request, 'spaceweather.html')
#redirect functions
def home_rdr(request):
    return redirect('/')
def about_rdr(request):
    return redirect('About/')
def data_rdr(request):
    return redirect('Data/')
def debris_rdr(request):
    return redirect('Debris/')
def weather_rdr(request):
    return redirect('Weather/')
def explore_rdr(request):
    return redirect('Explore/')


