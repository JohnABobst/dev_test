from django.contrib import admin
from django.urls import path
from matcher import views

app_name = 'matcher'
urlpatterns = [
    path('matcher', views.MatcherReportView.as_view(), name='match-reports'),
    path('select_match/<int:input_recording_id>/<int:match_id>', views.select_match, name='select-match'),
    
]
