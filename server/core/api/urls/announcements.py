from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListAnnouncement.as_view(), name='announcement-list'),
    path('<int:announcement_id>/', views.DetailAnnouncement.as_view(), name='announcement-detail'),
    path('create/', views.CreateAnnouncement.as_view(), name='announcement'),
    path('<int:announcement_id>/update/', views.UpdateAnnouncement.as_view(), name='announcement-update'),
]
