from django.urls import path, include
from . import events, sermons, series, resources, devotions, prayer_requests, reflections, announcements, live_streams, admins

urlpatterns = [
    path('events/', include(events.urlpatterns)),
    path('sermons/', include(sermons.urlpatterns)),
    path('series/', include(series.urlpatterns)),
    path('resources/', include(resources.urlpatterns)),
    path('devotions/', include(devotions.urlpatterns)),
    path('prayer-requests/', include(prayer_requests.urlpatterns)),
    path('reflections/', include(reflections.urlpatterns)),
    path('announcements/', include(announcements.urlpatterns)),
    path('live-streams/', include(live_streams.urlpatterns)),
    path('admins/', include(admins.urlpatterns)),


]
