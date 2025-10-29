from rest_framework import generics
from .models import Sermon, Resource, Series, Event, Devotion, Reflection, Prayer_request, Announcement, Live_stream
from .serializers import SermonSerializer, ResourceSerializer, SeriesSerializer,EventSerializer, DevotionSerializer, ReflectionSerializer, PrayerRequestSerializer, AnnouncementSerializer, LiveStreamSerializer, AdminUserSerializer
from rest_framework.permissions import IsAdminUser, AllowAny 
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema
from django.contrib.auth import get_user_model





@extend_schema(tags=['Sermons'])
class ListSermon(generics.ListAPIView):
    queryset = Sermon.objects.order_by('-date')
    serializer_class = SermonSerializer
    ordering = ['-date']
    filterset_fields = ['series__title', 'preacher']
    search_fields = ['title', 'description', 'preacher', 'series__title']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    

@extend_schema(tags=['Sermons'])
class DetailSermon(generics.RetrieveAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'

@extend_schema(tags=['Sermons'])
class CreateSermon(generics.CreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Sermons'])
class UpdateSermon(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'

    #Resources

@extend_schema(tags=['Resources'])
class ListResource(generics.ListAPIView):
    queryset = Resource.objects.order_by('-name')
    serializer_class = ResourceSerializer
    ordering = ['name']
    search_fields = ['name']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10


@extend_schema(tags=['Resources'])
class DetailResource(generics.RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

@extend_schema(tags=['Resources'])
class CreateResource(generics.CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Resources'])
class UpdateResource(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

    #series

@extend_schema(tags=['Series'])
class ListSeries(generics.ListAPIView):
    queryset = Series.objects.order_by('-date')
    serializer_class = SeriesSerializer
    ordering = ['-date']
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination
    

@extend_schema(tags=['Series'])
class DetailSeries(generics.RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

@extend_schema(tags=['Series'])
class CreateSeries(generics.CreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Series'])
class UpdateSeries(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

    #Events

@extend_schema(tags=['Events'])
class ListEvent(generics.ListAPIView):
    queryset = Event.objects.order_by('date')
    serializer_class = EventSerializer
    ordering = ['-date', '-start_time']
    search_fields = ['name', 'description', 'location']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    

@extend_schema(tags=['Events'])
class DetailEvent(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'

@extend_schema(tags=['Events'])
class CreateEvent(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Events'])
class UpdateEvent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'


#Devotions
@extend_schema(tags=['Devotions'])
class ListDevotion(generics.ListAPIView):
    queryset = Devotion.objects.order_by('-date')
    serializer_class = DevotionSerializer
    ordering = ['-date']
    search_fields = ['title', 'Bible_verse', 'content', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

@extend_schema(tags=['Devotions'])
class DetailDevotion(generics.RetrieveAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'devotion_id'

@extend_schema(tags=['Devotions'])
class CreateDevotion(generics.CreateAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Devotions'])
class UpdateDevotion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devotion.objects.all()
    serializer_class = DevotionSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'devotion_id'

#Reflections
@extend_schema(tags=['Reflections'])
class ListReflection(generics.ListAPIView):
    queryset = Reflection.objects.order_by('-date')
    serializer_class = ReflectionSerializer
    ordering = ['-date']
    search_fields = ['name', 'content', 'date', 'devotion__title']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

@extend_schema(tags=['Reflections'])
class DetailReflection(generics.RetrieveAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'reflection_id'

@extend_schema(tags=['Reflections'])
class CreateReflection(generics.CreateAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Reflections'])
class UpdateReflection(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reflection.objects.all()
    serializer_class = ReflectionSerializer
    permission_classes = []
    lookup_field = 'id'
    lookup_url_kwarg = 'reflection_id'

@extend_schema(tags=['Prayer Requests'])
class ListPrayerRequest(generics.ListAPIView):
    queryset = Prayer_request.objects.order_by('-date')
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    ordering = ['-date']
    search_fields = ['name', 'subject', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

@extend_schema(tags=['Prayer Requests'])
class DetailPrayerRequest(generics.RetrieveAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'prayer_request_id'

@extend_schema(tags=['Prayer Requests'])
class CreatePrayerRequest(generics.CreateAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Prayer Requests'])
class DeletePrayerRequest(generics.RetrieveDestroyAPIView):
    queryset = Prayer_request.objects.all()
    serializer_class = PrayerRequestSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'prayer_request_id'

@extend_schema(tags=['Announcements'])
class ListAnnouncement(generics.ListAPIView):
    queryset = Announcement.objects.order_by('-date')
    serializer_class = AnnouncementSerializer
    ordering = ['-date']
    search_fields = ['title', 'content', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

@extend_schema(tags=['Announcements'])
class DetailAnnouncement(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'announcement_id'

@extend_schema(tags=['Announcements'])
class CreateAnnouncement(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Announcements'])
class UpdateAnnouncement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'announcement_id'


#Live Streams
@extend_schema(tags=['Live Streams'])
class ListLiveStream(generics.ListAPIView):
    queryset = Live_stream.objects.order_by('-date')
    serializer_class = LiveStreamSerializer
    ordering = ['-date']
    search_fields = ['title', 'description', 'status', 'date']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

@extend_schema(tags=['Live Streams'])
class DetailLiveStream(generics.RetrieveAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'live_stream_id'

@extend_schema(tags=['Live Streams'])
class CreateLiveStream(generics.CreateAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Live Streams'])
class UpdateLiveStream(generics.RetrieveUpdateDestroyAPIView):
    queryset = Live_stream.objects.all()
    serializer_class = LiveStreamSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'live_stream_id'


@extend_schema(tags=['Admin'])
class CreateAdminUser(generics.CreateAPIView):
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return get_user_model().objects.none()


@extend_schema(tags=['Admin'])
class DeleteAdminUser(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        User = get_user_model()
        return User.objects.filter(is_staff=True)

    def get_object(self):
        User = get_user_model()
        return generics.get_object_or_404(self.get_queryset(), pk=self.kwargs.get('user_id'))

    def perform_destroy(self, instance):
        # Prevent deleting self to avoid locking out the only admin
        request_user = self.request.user
        if instance.pk == getattr(request_user, 'pk', None):
            from rest_framework.exceptions import ValidationError
            raise ValidationError('Admins cannot delete their own account.')
        instance.delete()

