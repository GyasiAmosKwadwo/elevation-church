from rest_framework import generics
from .models import Sermon, Resource, Series, Event, Devotion, Reflection, Prayer_request, Announcement, Live_stream
from .serializers import SermonSerializer, ResourceSerializer, SeriesSerializer,EventSerializer, DevotionSerializer, ReflectionSerializer, PrayerRequestSerializer, AnnouncementSerializer, LiveStreamSerializer
from rest_framework.permissions import IsAdminUser, AllowAny 
from rest_framework.pagination import PageNumberPagination





class ListSermon(generics.ListAPIView):
    queryset = Sermon.objects.order_by('-date')
    serializer_class = SermonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'
    ordering = ['-date']
    filterset_fields = ['series__title', 'preacher']
    search_fields = ['title', 'description', 'preacher', 'series__title']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    

class DetailSermon(generics.RetrieveAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'

class CreateSermon(generics.CreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]

class UpdateSermon(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'

    #Resources

class ListResource(generics.ListAPIView):
    queryset = Resource.objects.order_by('-name')
    serializer_class = ResourceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'
    ordering = ['name']
    search_fields = ['name']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10


class DetailResource(generics.RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

class CreateResource(generics.CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]

class UpdateResource(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

    #series

class ListSeries(generics.ListAPIView):
    queryset = Series.objects.order_by('-date')
    serializer_class = SeriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'
    ordering = ['-date']
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination
    

class DetailSeries(generics.RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

class CreateSeries(generics.CreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]

class UpdateSeries(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

    #Events

class ListEvent(generics.ListAPIView):
    queryset = Event.objects.order_by('date')
    serializer_class = EventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    ordering = ['-date', '-start_time']
    search_fields = ['name', 'description', 'location']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    

class DetailEvent(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'

class CreateEvent(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]

class UpdateEvent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'


#Devotions
class ListDevotion(generics.ListAPIView):
    queryset = Devotion.objects.order_by('-date')
    serializer_class = DevotionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'devotion_id'
    ordering = ['-date']
    search_fields = ['title', 'Bible_verse', 'content', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

class DetailDevotion(generics.RetrieveAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'devotion_id'

class CreateDevotion(generics.CreateAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    permission_classes = [IsAdminUser]

class UpdateDevotion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'devotion_id'

#Reflections
class ListReflection(generics.ListAPIView):
    queryset = Reflection.objects.order_by('-date')
    serializer_class = ReflectionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'reflection_id'
    ordering = ['-date']
    search_fields = ['name', 'content', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

class DetailReflection(generics.RetrieveAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'reflection_id'

class CreateReflection(generics.CreateAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = []

class UpdateReflection(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = []
    lookup_field = 'id'
    lookup_url_kwarg = 'reflection_id'

class ListPrayerRequest(generics.ListAPIView):
    queryset = Prayer_request.objects.order_by('-date')
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'prayer_request_id'
    ordering = ['-date']
    search_fields = ['name', 'subject', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

class DetailPrayerRequest(generics.RetrieveAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'prayer_request_id'

class CreatePrayerRequest(generics.CreateAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [AllowAny]

class DeletePrayerRequest(generics.RetrieveDestroyAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'prayer_request_id'

class ListAnnouncement(generics.ListAPIView):
    queryset = Announcement.objects.order_by('-date')
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'announcement_id'
    ordering = ['-date']
    search_fields = ['title', 'content', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

class DetailAnnouncement(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'announcement_id'

class CreateAnnouncement(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]

class UpdateAnnouncement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'announcement_id'


#Live Streams
class ListLiveStream(generics.ListAPIView):
    queryset = Live_stream.objects.order_by('-date')
    serializer_class = LiveStreamSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'live_stream_id'
    ordering = ['-date']
    search_fields = ['title', 'description', 'status', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

class DetailLiveStream(generics.RetrieveAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'live_stream_id'

class CreateLiveStream(generics.CreateAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    permission_classes = [IsAdminUser]

class UpdateLiveStream(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'live_stream_id'

