
from django.urls import path 
from . import views



urlpatterns = [
    path('', views.receipes, name="home"),
    path('delete_receipe/<id>/', views.delete_receipe, name="delete_receipe"),
    path('update_receipe/<id>/', views.update_receipe, name="update_receipe"),
    
]