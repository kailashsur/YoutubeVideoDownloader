from django.urls import path
from . import views

urlpatterns = [
    path('', views.download_video, name='download_video'),  # Map the home page to the download_video view
]
