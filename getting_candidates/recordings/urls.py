from django.contrib import admin
from django.urls import path
from recordings import views

app_name = 'recordings'
urlpatterns = [
    path('recordings/', views.RecordingView.as_view(), name='recordings-list'),
    path('upload', views.upload_view, name='upload'),
    path('add_song', views.add_song, name='add_song')
]
