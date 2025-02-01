from django.urls import path
from . import views


urlpatterns = [
    path('upload-planilha/', views.upload_planilha, name='upload_planilha'),
    path('download-planilha/', views.download_planilha, name='download_planilha'),
]
