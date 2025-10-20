from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListPrayerRequest.as_view(), name='prayer-request-list'),
    path('<uuid:prayer_request_id>/', views.DetailPrayerRequest.as_view(), name='prayer-request-detail'),
    path('create/', views.CreatePrayerRequest.as_view(), name='prayer-request'),
    path('<uuid:prayer_request_id>/delete/', views.DeletePrayerRequest.as_view(), name='prayer-request-delete'),
]
