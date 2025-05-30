from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),  # URL pattern for the index view
    path('about/', views.about, name='about'),  # URL pattern for the about view
    path('category/<slug:category_name_slug>/',
         views.show_category, name = 'show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
] 