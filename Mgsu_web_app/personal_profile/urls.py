from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.profile),
    path('logout/', views.logout_view, name='logout'),
    # path('news/', LogoutView.as_view(next_page='/'), name='news'),
]