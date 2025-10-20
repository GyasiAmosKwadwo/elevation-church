from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListSermon.as_view(), name='sermon-list'),
    path('<uuid:sermon_id>/', views.DetailSermon.as_view(), name='sermon-detail'),
    path('create/', views.CreateSermon.as_view(), name='sermon'),
    path('<uuid:sermon_id>/update/', views.UpdateSermon.as_view(), name='sermon-update'),
]
