from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutrdr(request):
    return redirect('About/')
def home(request):
    return redirect('/')
def about(request):
    return render(request, 'about.html')
def more(request):
    return render(request, 'more.html')
def data(request):
    return render(request, 'data.html')
def explore(request):
    return render(request, 'explore.html')

