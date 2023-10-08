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
#redirect functions
def home_rdr(request):
    return redirect('/')
def about_rdr(request):
    return redirect('About/')
def data_rdr(request):
    return redirect('Data/')
def debris_rdr(request):
    return redirect('Debris/')
def explore_rdr(request):
    return redirect('Explore/')


