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
    #Devotions
    path('devotions/', views.ListDevotion.as_view(), name='devotion-list'),
    path('devotions/<int:devotion_id>/', views.DetailDevotion.as_view(), name='devotion-detail'),
    path('devotions/create/', views.CreateDevotion.as_view(), name='devotion'),
    path('devotions/<int:devotion_id>/update/', views.UpdateDevotion.as_view(), name='devotion-update'),
    #Reflections
    path('reflections/', views.ListReflection.as_view(), name='reflection-list'),
    path('reflections/<int:reflection_id>/', views.DetailReflection.as_view(), name='reflection-detail'),
    path('reflections/create/', views.CreateReflection.as_view(), name='reflection'),
    path('reflections/<int:reflection_id>/update/', views.UpdateReflection.as_view(), name='reflection-update'),

    #Prayer Requests
    path('prayer-requests/', views.ListPrayerRequest.as_view(), name='prayer-request-list'),
    path('prayer-requests/<int:prayer_request_id>/', views.DetailPrayerRequest.as_view(), name='prayer-request-detail'),
    path('prayer-requests/create/', views.CreatePrayerRequest.as_view(), name='prayer-request'),
    path('prayer-requests/<int:prayer_request_id>/delete/', views.DeletePrayerRequest.as_view(), name='prayer-request-delete'), 

    #Announcements
    path('announcements/', views.ListAnnouncement.as_view(), name='announcement-list'),
    path('announcements/<int:announcement_id>/', views.DetailAnnouncement.as_view(), name='announcement-detail'),
    path('announcements/create/', views.CreateAnnouncement.as_view(), name='announcement'),     
    path('announcements/<int:announcement_id>/update/', views.UpdateAnnouncement.as_view(), name='announcement-update'),
      


    
]