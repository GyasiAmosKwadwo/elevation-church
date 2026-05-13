from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListReel.as_view(), name='reel-list'),
    path('<uuid:reel_id>/', views.DetailReel.as_view(), name='reel-detail'),
    path('create/', views.CreateReel.as_view(), name='reel-create'),
    path('<uuid:reel_id>/update/', views.UpdateReel.as_view(), name='reel-update'),
]
