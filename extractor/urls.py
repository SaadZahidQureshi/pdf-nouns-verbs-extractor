from django.urls import path
from .views import ExtractedDataView
from . import views

urlpatterns = [
    path('api/extracted_data/', ExtractedDataView.as_view(), name='extracted_data'),
    path('', views.index, name='index'),
]
