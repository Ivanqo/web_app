from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)