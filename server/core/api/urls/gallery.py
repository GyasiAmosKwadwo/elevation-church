from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListGalleryImage.as_view(), name='gallery-image-list'),
    path('<uuid:gallery_image_id>/', views.DetailGalleryImage.as_view(), name='gallery-image-detail'),
    path('create/', views.CreateGalleryImage.as_view(), name='gallery-image-create'),
    path('<uuid:gallery_image_id>/update/', views.UpdateGalleryImage.as_view(), name='gallery-image-update'),

    path('albums/', views.ListGallery.as_view(), name='gallery-list'),
    path('albums/<uuid:gallery_id>/', views.DetailGallery.as_view(), name='gallery-detail'),
    path('albums/create/', views.CreateGallery.as_view(), name='gallery-create'),
    path('albums/<uuid:gallery_id>/update/', views.UpdateGallery.as_view(), name='gallery-update'),
]
