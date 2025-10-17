from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListSermon.as_view(), name='sermon-list'),
    path('<int:sermon_id>/', views.DetailSermon.as_view(), name='sermon-detail'),
    path('create/', views.CreateSermon.as_view(), name='sermon'),
    path('<int:sermon_id>/update/', views.UpdateSermon.as_view(), name='sermon-update'),
]
