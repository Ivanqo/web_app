from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.first, name = 'auth'),
    path('pwa', views.login_view, name = 'auth'),
]