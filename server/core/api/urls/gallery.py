from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListGalleryImage.as_view(), name='gallery-image-list'),
    path('<uuid:gallery_image_id>/', views.DetailGalleryImage.as_view(), name='gallery-image-detail'),
    path('create/', views.CreateGalleryImage.as_view(), name='gallery-image-create'),
    path('<uuid:gallery_image_id>/update/', views.UpdateGalleryImage.as_view(), name='gallery-image-update'),
]