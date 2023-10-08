from django.urls import path
from . import views

#page urls
urlpatterns = [
    path('', views.index, name = 'index'),
    path('About/', views.about, name='About'),
    path('More/', views.more, name = 'More'),
    path('Data/', views.data, name = 'Data'),
    path('Explore/', views.explore, name = 'Explore'),
    path('Debris/', views.debris, name = 'Debris'),
    path('Weather/', views.weather, name = 'Weather'),

    # redirect

    path('Home/', views.home_rdr, name='Home'),
    path('About/', views.about_rdr, name='About'),
    path('Data/', views.data_rdr, name='Data'),
    path('Debris/', views.debris_rdr, name='Debris'),
    path('Weather/', views.weather_rdr, name = 'Weather')
]