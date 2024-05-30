from django.urls import path
from .views import ExtractedDataView
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('api/extracted_data',ExtractedDataView,'api')


urlpatterns = [
    path('api/extracted_data/', ExtractedDataView.as_view(), name='extracted_data'),
    path('', views.index, name='index'),
]
