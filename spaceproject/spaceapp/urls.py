from django.urls import path
from . import views

#page urls
urlpatterns = [
    path('', views.index, name = 'index'),
    path('Home/', views.home, name='Home'),
    path('About/', views.about, name='About'),
    path('About/', views.aboutrdr, name='About'),
    path('More/', views.more, name = 'More'),
    path('Data/', views.data, name = 'Data'),
    path('Explore/', views.explore, name = 'Explore')
    
]