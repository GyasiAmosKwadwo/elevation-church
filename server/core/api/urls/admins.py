from django.urls import path
from api import views

urlpatterns = [
    path('create/', views.CreateStaffUser.as_view(), name='staff-create'),
    path('<int:user_id>/delete/', views.DeleteStaffUser.as_view(), name='staff-delete'),
]
