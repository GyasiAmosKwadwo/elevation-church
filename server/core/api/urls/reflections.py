from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListReflection.as_view(), name='reflection-list'),
    path('<uuid:reflection_id>/', views.DetailReflection.as_view(), name='reflection-detail'),
    path('create/', views.CreateReflection.as_view(), name='reflection'),
    path('<uuid:reflection_id>/update/', views.UpdateReflection.as_view(), name='reflection-update'),
    path('devotion/<uuid:devotion_id>/', views.get_reflections_for_devotion.as_view(), name='reflections-for-devotion'),
]
