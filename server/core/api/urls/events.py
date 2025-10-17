from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListEvent.as_view(), name='event-list'),
    path('<int:event_id>/', views.DetailEvent.as_view(), name='event-detail'),
    path('create/', views.CreateEvent.as_view(), name='event'),
    path('<int:event_id>/update/', views.UpdateEvent.as_view(), name='event-update'),
]
