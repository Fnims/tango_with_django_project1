from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('about/', views.about, name='about'),  # URL pattern for the about view
] 