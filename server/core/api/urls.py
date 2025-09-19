from django.urls import path
from . import views



urlpatterns = [
    path('sermons/', views.ListSermon.as_view(), name='sermon-list'),
    path('sermons/<int:sermon_id>/', views.DetailSermon.as_view(), name='sermon-detail'),
    path('sermons/create/', views.CreateSermon.as_view(), name='sermon'),
    path('sermons/<int:sermon_id>/update/', views.UpdateSermon.as_view(), name='sermon-update'),
    #Resources
    path('resources/', views.ListResource.as_view(), name='resource-list'),
    path('resources/<int:resource_id>/', views.DetailResource.as_view(), name='resource-detail'),
    path('resources/create/', views.CreateResource.as_view(), name='resource'),
    path('resources/<int:resource_id>/update/', views.UpdateResource.as_view(), name='resource-update'),
    #Series
    path('series/', views.ListSeries.as_view(), name='series-list'),
    path('series/<int:series_id>/', views.DetailSeries.as_view(), name='series-detail'),
    path('series/create/', views.CreateSeries.as_view(), name='series'),
    path('series/<int:series_id>/update/', views.UpdateSeries.as_view(), name='series-update'),
    #Events
    path('events/', views.ListEvent.as_view(), name='event-list'),
    path('events/<int:event_id>/', views.DetailEvent.as_view(), name='event-detail'),
    path('events/create/', views.CreateEvent.as_view(), name='event'),
    path('events/<int:event_id>/update/', views.UpdateEvent.as_view(), name='event-update'),
    
]