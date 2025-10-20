from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListResource.as_view(), name='resource-list'),
    path('<uuid:resource_id>/', views.DetailResource.as_view(), name='resource-detail'),
    path('create/', views.CreateResource.as_view(), name='resource'),
    path('<uuid:resource_id>/update/', views.UpdateResource.as_view(), name='resource-update'),
]
