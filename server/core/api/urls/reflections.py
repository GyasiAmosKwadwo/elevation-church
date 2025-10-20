from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListReflection.as_view(), name='reflection-list'),
    path('<uuid:reflection_id>/', views.DetailReflection.as_view(), name='reflection-detail'),
    path('create/', views.CreateReflection.as_view(), name='reflection'),
    path('<uuid:reflection_id>/update/', views.UpdateReflection.as_view(), name='reflection-update'),
]
