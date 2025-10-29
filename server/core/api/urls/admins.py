from django.urls import path
from api import views

urlpatterns = [
    path('create/', views.CreateAdminUser.as_view(), name='admin-create'),
    path('<int:user_id>/delete/', views.DeleteAdminUser.as_view(), name='admin-delete'),
]
