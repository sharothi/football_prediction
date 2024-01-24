from django.urls import path
from . import views

urlpatterns = [
    # path('predict/', views.predict_results, name='predict_results'),
    path('upload-csv/', views.upload_csv, name='upload_csv'),
    path('upload-success/', views.upload_success, name='upload_success'),
    path('read_data/', views.read_data, name='read_data'),
    path('team_status/',views.team_status, name='team_status'),
    path('compersion/', views.compersion, name='compersion'),
]
