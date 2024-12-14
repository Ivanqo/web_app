from django.urls import path
from . import views
 
urlpatterns = [
   path(
       "",
       views.NewListView.as_view(),
       name="new-list"
   ),
   path(
       "new/<int:pk>",
       views.NewDetailView.as_view(),
       name="new-detail"
   ),
]