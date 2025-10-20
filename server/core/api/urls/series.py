from django.urls import path
from api import views

urlpatterns = [
    path('', views.ListSeries.as_view(), name='series-list'),
    path('<uuid:series_id>/', views.DetailSeries.as_view(), name='series-detail'),
    path('create/', views.CreateSeries.as_view(), name='series'),
    path('<uuid:series_id>/update/', views.UpdateSeries.as_view(), name='series-update'),
]
