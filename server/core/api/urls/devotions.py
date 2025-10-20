from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListDevotion.as_view(), name='devotion-list'),
    path('<uuid:devotion_id>/', views.DetailDevotion.as_view(), name='devotion-detail'),
    path('create/', views.CreateDevotion.as_view(), name='devotion'),
    path('<uuid:devotion_id>/update/', views.UpdateDevotion.as_view(), name='devotion-update'),
]
