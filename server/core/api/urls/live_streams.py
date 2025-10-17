from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListLiveStream.as_view(), name='live-stream-list'),
    path('<int:live_stream_id>/', views.DetailLiveStream.as_view(), name='live-stream-detail'),
    path('create/', views.CreateLiveStream.as_view(), name='live-stream'),
    path('<int:live_stream_id>/update/', views.UpdateLiveStream.as_view(), name='live-stream-update'),
]
