from django.urls import path
from . import views

#page urls
urlpatterns = [
    path('', views.index, name = 'index'),
    path('Home/', views.home, name='Home'),
    path('about/', views.about, name = 'about'),
    path('seemore/', views.seemore, name = 'seemore'),
    path('seedata/', views.seedata, name = 'seedata'),
    path('explore/', views.explore, name = 'explore')
    
]