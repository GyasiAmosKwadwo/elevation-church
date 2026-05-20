from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Sermon, 
    Resource, 
    Series, 
    Event, 
    Devotion, 
    BiblePassageCache,
    Reflection, 
    Prayer_request, 
    Announcement, 
    Live_stream, 
    Gallery,
    GalleryImage,
    ContributionChannel,
    ContributionIntent,
    Reel,
    SiteSettings,
    ThemeSettings,
    NavigationItem,
    PageConfig,
    SectionConfig,
    )
from .serializers import ( 
    SermonSerializer, 
    ResourceSerializer, 
    SeriesSerializer,
    EventSerializer, 
    DevotionSerializer, 
    ReflectionSerializer, 
    PrayerRequestSerializer, 
    AnnouncementSerializer,
    LiveStreamSerializer,
    BiblePassageSerializer,
    StaffUserSerializer, 
    GallerySerializer,
    GalleryImageSerializer,
    ContributionChannelSerializer,
    ContributionIntentSerializer,
    ReelSerializer,
    SiteSettingsSerializer,
    ThemeSettingsSerializer,
    NavigationItemSerializer,
    PageConfigSerializer,
    SectionConfigSerializer,
    )
from .bible_service import fetch_bible_passage
from rest_framework.permissions import IsAdminUser, AllowAny, BasePermission, SAFE_METHODS
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.contrib.auth import get_user_model
from rest_framework import parsers
from django.utils import timezone
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncDate
from datetime import timedelta


@extend_schema(tags=['Sermons'], description="Retrieve a list of sermons ordered by date.")
class ListSermon(generics.ListAPIView):
    queryset = Sermon.objects.order_by('-date')
    serializer_class = SermonSerializer
    ordering = ['-date']
    filterset_fields = ['series__title', 'preacher']
    search_fields = ['title', 'description', 'preacher', 'series__title']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    

@extend_schema(tags=['Sermons'], description="Retrieve details of a specific sermon by its ID.")
class DetailSermon(generics.RetrieveAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'

@extend_schema(tags=['Sermons'], description="Create a new sermon entry. Admin access required.")
class CreateSermon(generics.CreateAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Sermons'], description="Update or delete an existing sermon by its ID. Admin access required.")
class UpdateSermon(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'sermon_id'


    #Resources

@extend_schema(tags=['Resources'], description="Retrieve a list of resources ordered by name.")
class ListResource(generics.ListAPIView):
    queryset = Resource.objects.order_by('-name')
    serializer_class = ResourceSerializer
    ordering = ['name']
    search_fields = ['name']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10


@extend_schema(tags=['Resources'], description="Retrieve details of a specific resource by its ID.")
class DetailResource(generics.RetrieveAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

@extend_schema(tags=['Resources'], description="Create a new resource entry. Admin access required.")
class CreateResource(generics.CreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Resources'], description="Update or delete an existing resource by its ID. Admin access required.")
class UpdateResource(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'resource_id'

    #series

@extend_schema(tags=['Series'], description="Retrieve a list of series ordered by date.")
class ListSeries(generics.ListAPIView):
    queryset = Series.objects.order_by('-date')
    serializer_class = SeriesSerializer
    ordering = ['-date']
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination
    

@extend_schema(tags=['Series'], description="Retrieve details of a specific series by its ID.")
class DetailSeries(generics.RetrieveAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

@extend_schema(tags=['Series'], description="Create a new series entry. Admin access required.")
class CreateSeries(generics.CreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Series'], description="Update or delete an existing series by its ID. Admin access required.")
class UpdateSeries(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'series_id'

    #Events

@extend_schema(tags=['Events'], description="Retrieve a list of events ordered by date.")
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


@extend_schema(
    tags=['Bible'],
    summary='Fetch a Bible passage by reference',
    description='Return one Bible passage from the external Bible API. The reference query parameter is required.',
    responses=BiblePassageSerializer,
    parameters=[
        OpenApiParameter(
            name='reference',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Bible passage reference to fetch, for example "John 3:16" or "John 3".',
            required=True,
        ),
        OpenApiParameter(
            name='translation',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Optional Bible translation code. Default is kjv. Supported values depend on the external API.',
            required=False,
        ),
    ],
)
class BiblePassageDetail(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = BiblePassageSerializer

    def get(self, request):
        reference = request.query_params.get('reference', '').strip()
        translation = request.query_params.get('translation', 'kjv').strip().lower() or 'kjv'

        if not reference:
            return Response({'detail': 'The reference query parameter is required.'}, status=400)

        cached_passage = BiblePassageCache.objects.filter(reference__iexact=reference, translation=translation).first()
        if cached_passage is not None:
            serializer = BiblePassageSerializer(cached_passage)
            return Response(serializer.data)

        passage_data = fetch_bible_passage(reference, translation)
        cached_passage = BiblePassageCache.objects.create(
            reference=reference,
            translation=translation,
            passage_text=passage_data['passage_text'],
            raw_response=passage_data['raw_response'],
        )
        serializer = BiblePassageSerializer(cached_passage)
        return Response(serializer.data)


@extend_schema(
    tags=['Bible'],
    summary='Search cached Bible passages',
    description='Search the locally cached Bible passage results by reference or passage text. Use query or reference to filter results.',
    responses=BiblePassageSerializer,
    parameters=[
        OpenApiParameter(
            name='query',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Text search term for passage content or reference. Optional.',
            required=False,
        ),
        OpenApiParameter(
            name='reference',
            type=str,
            location=OpenApiParameter.QUERY,
            description='Partial or full Bible reference to filter cached passages. Optional.',
            required=False,
        ),
    ],
)
class BiblePassageSearch(generics.ListAPIView):
    queryset = BiblePassageCache.objects.order_by('-fetched_at')
    serializer_class = BiblePassageSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('query', '').strip()
        reference = self.request.query_params.get('reference', '').strip()

        if reference:
            queryset = queryset.filter(reference__icontains=reference)
        if query:
            queryset = queryset.filter(Q(reference__icontains=query) | Q(passage_text__icontains=query))

        return queryset


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

@extend_schema(tags=['Reflections'])
class get_reflections_for_devotion(generics.ListAPIView):
    serializer_class = ReflectionSerializer
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10

    def get_queryset(self):
        devotion_id = self.kwargs['devotion_id']
        return Reflection.objects.filter(devotion__id=devotion_id).order_by('-date')

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


class SingletonRetrieveUpdateMixin(generics.RetrieveUpdateAPIView):
    singleton_model = None

    def get_object(self):
        if self.singleton_model is None:
            raise AttributeError("singleton_model must be set")
        obj, _ = self.singleton_model.objects.get_or_create(pk=1)
        return obj


@extend_schema(tags=['Site Config'], description="Get and update global site settings.")
class RetrieveUpdateSiteSettings(SingletonRetrieveUpdateMixin):
    serializer_class = SiteSettingsSerializer
    permission_classes = [AllowAny]
    singleton_model = SiteSettings

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAdminUser()]


@extend_schema(tags=['Site Config'], description="Get and update global theme settings.")
class RetrieveUpdateThemeSettings(SingletonRetrieveUpdateMixin):
    serializer_class = ThemeSettingsSerializer
    permission_classes = [IsAdminUser]
    singleton_model = ThemeSettings


@extend_schema(tags=['Site Config'], description="List and create navigation items.")
class ListCreateNavigationItem(generics.ListCreateAPIView):
    queryset = NavigationItem.objects.select_related('parent').order_by('location', 'display_order', 'label')
    serializer_class = NavigationItemSerializer
    permission_classes = [IsAdminUser]
    ordering = ['location', 'display_order', 'label']
    search_fields = ['label', 'url', 'location', 'item_type']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 50


@extend_schema(tags=['Site Config'], description="Retrieve, update, or delete one navigation item.")
class DetailUpdateNavigationItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = NavigationItem.objects.select_related('parent').all()
    serializer_class = NavigationItemSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'


@extend_schema(tags=['Site Config'], description="List and create page configs.")
class ListCreatePageConfig(generics.ListCreateAPIView):
    queryset = PageConfig.objects.order_by('display_order', 'slug')
    serializer_class = PageConfigSerializer
    permission_classes = [IsAdminUser]
    ordering = ['display_order', 'slug']
    search_fields = ['slug', 'title', 'subtitle']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 50


@extend_schema(tags=['Site Config'], description="Retrieve, update, or delete one page config.")
class DetailUpdatePageConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = PageConfig.objects.all()
    serializer_class = PageConfigSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


@extend_schema(tags=['Site Config'], description="List and create section configs.")
class ListCreateSectionConfig(generics.ListCreateAPIView):
    serializer_class = SectionConfigSerializer
    permission_classes = [IsAdminUser]
    ordering = ['page__slug', 'display_order', 'key']
    search_fields = ['key', 'title', 'page__slug']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 100

    def get_queryset(self):
        queryset = SectionConfig.objects.select_related('page').order_by('page__slug', 'display_order', 'key')
        page_slug = self.request.query_params.get('page')
        if page_slug:
            queryset = queryset.filter(page__slug=page_slug)
        return queryset


@extend_schema(tags=['Site Config'], description="Retrieve, update, or delete one section config.")
class DetailUpdateSectionConfig(generics.RetrieveUpdateDestroyAPIView):
    queryset = SectionConfig.objects.select_related('page').all()
    serializer_class = SectionConfigSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'section_id'


@extend_schema(tags=['Site Config'], description="Public endpoint to load all site appearance/content configuration.")
class PublicSiteConfiguration(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        site = SiteSettingsSerializer(SiteSettings.load()).data
        theme = ThemeSettingsSerializer(ThemeSettings.load()).data

        navigation_queryset = NavigationItem.objects.filter(
            is_enabled=True,
            parent__isnull=True
        ).order_by('location', 'display_order', 'label')
        navigation = NavigationItemSerializer(navigation_queryset, many=True).data

        pages_queryset = PageConfig.objects.filter(is_enabled=True).prefetch_related('sections').order_by(
            'display_order', 'slug'
        )
        pages = PageConfigSerializer(pages_queryset, many=True).data

        return Response({
            "site": site,
            "theme": theme,
            "navigation": navigation,
            "pages": pages,
        })


# Contributions
@extend_schema(tags=['Contributions'], description="List active contribution channels for users.")
class ListContributionChannel(generics.ListAPIView):
    serializer_class = ContributionChannelSerializer
    permission_classes = [AllowAny]
    ordering = ['display_order', 'name']
    search_fields = ['name', 'account_name', 'account_number', 'bank_name', 'network']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 20

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return ContributionChannel.objects.order_by('display_order', 'name')
        return ContributionChannel.objects.filter(is_active=True).order_by('display_order', 'name')


@extend_schema(tags=['Contributions'], description="Retrieve details of a contribution channel.")
class DetailContributionChannel(generics.RetrieveAPIView):
    serializer_class = ContributionChannelSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    lookup_url_kwarg = 'channel_id'

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return ContributionChannel.objects.all()
        return ContributionChannel.objects.filter(is_active=True)


@extend_schema(tags=['Contributions'], description="Create a contribution channel. Staff/Admin only.")
class CreateContributionChannel(generics.CreateAPIView):
    queryset = ContributionChannel.objects.all()
    serializer_class = ContributionChannelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['Contributions'], description="Update or delete a contribution channel. Staff/Admin only.")
class UpdateContributionChannel(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContributionChannel.objects.all()
    serializer_class = ContributionChannelSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'channel_id'


@extend_schema(tags=['Contributions'], description="Create a contribution intent after user transfers via MOMO/BANK.")
class CreateContributionIntent(generics.CreateAPIView):
    queryset = ContributionIntent.objects.all()
    serializer_class = ContributionIntentSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=['Contributions'], description="List contribution intents. Staff/Admin only.")
class ListContributionIntent(generics.ListAPIView):
    queryset = ContributionIntent.objects.select_related('channel', 'confirmed_by').order_by('-created_at')
    serializer_class = ContributionIntentSerializer
    permission_classes = [IsAdminUser]
    ordering = ['-created_at']
    search_fields = ['donor_name', 'donor_phone', 'reference', 'channel__name']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 20


@extend_schema(tags=['Contributions'], description="Retrieve one contribution intent. Staff/Admin only.")
class DetailContributionIntent(generics.RetrieveAPIView):
    queryset = ContributionIntent.objects.select_related('channel', 'confirmed_by').all()
    serializer_class = ContributionIntentSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'intent_id'


@extend_schema(tags=['Contributions'], description="Update contribution intent status/admin note. Staff/Admin only.")
class UpdateContributionIntent(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContributionIntent.objects.select_related('channel', 'confirmed_by').all()
    serializer_class = ContributionIntentSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'intent_id'


# Reels
@extend_schema(tags=['Reels'], description="List reels for users (published reels) and staff (all reels).")
class ListReel(generics.ListAPIView):
    serializer_class = ReelSerializer
    permission_classes = [AllowAny]
    ordering = ['-published_at', '-created_at']
    search_fields = ['title', 'caption', 'category']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 20

    def get_queryset(self):
        queryset = Reel.objects.order_by('-published_at', '-created_at')
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return queryset
        return queryset.filter(is_published=True)


@extend_schema(tags=['Reels'], description="Retrieve a reel.")
class DetailReel(generics.RetrieveAPIView):
    serializer_class = ReelSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'
    lookup_url_kwarg = 'reel_id'

    def get_queryset(self):
        queryset = Reel.objects.all()
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return queryset
        return queryset.filter(is_published=True)


@extend_schema(tags=['Reels'], description="Create reel. Staff/Admin only.")
class CreateReel(generics.CreateAPIView):
    queryset = Reel.objects.all()
    serializer_class = ReelSerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['Reels'], description="Update or delete reel. Staff/Admin only.")
class UpdateReel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reel.objects.all()
    serializer_class = ReelSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'reel_id'


class SuperUserOnly(BasePermission):
    def has_permission(self, request, view):
        u = request.user
        return bool(u and u.is_authenticated and u.is_superuser)


@extend_schema(tags=['Staff'])
class CreateStaffUser(generics.CreateAPIView):
    serializer_class = StaffUserSerializer
    permission_classes = [SuperUserOnly]

    def get_queryset(self):
        return get_user_model().objects.none()


@extend_schema(tags=['Staff'])
class DeleteStaffUser(generics.DestroyAPIView):
    permission_classes = [SuperUserOnly]

    def get_queryset(self):
        User = get_user_model()
        return User.objects.filter(is_staff=True)

    def get_object(self):
        User = get_user_model()
        return generics.get_object_or_404(self.get_queryset(), pk=self.kwargs.get('user_id'))

    def perform_destroy(self, instance):
        request_user = self.request.user
        if instance.pk == getattr(request_user, 'pk', None):
            from rest_framework.exceptions import ValidationError
            raise ValidationError('You cannot delete your own account.')
        instance.delete()

@extend_schema(tags=['Galleries'])
class ListGallery(generics.ListAPIView):
    queryset = Gallery.objects.order_by('-date')
    serializer_class = GallerySerializer
    ordering = ['-date']
    search_fields = ['title', 'description', 'venue']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10


@extend_schema(tags=['Galleries'])
class DetailGallery(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'gallery_id'


@extend_schema(tags=['Galleries'])
class CreateGallery(generics.CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAdminUser]


@extend_schema(tags=['Galleries'])
class UpdateGallery(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'gallery_id'


@extend_schema(tags=['Gallery Images'])
class ListGalleryImage(generics.ListAPIView):
    queryset = GalleryImage.objects.order_by('-date')
    serializer_class = GalleryImageSerializer
    ordering = ['-date']
    search_fields = ['title', 'description', 'gallery__title']
    pagination_class = PageNumberPagination
    PageNumberPagination.page_size = 10
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

@extend_schema(tags=['Gallery Images'])
class DetailGalleryImage(generics.RetrieveAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'gallery_image_id'

@extend_schema(tags=['Gallery Images'])
class CreateGalleryImage(generics.CreateAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAdminUser]

@extend_schema(tags=['Gallery Images'], description="Update or delete an existing gallery image by its ID. Admin access required.")
class UpdateGalleryImage(generics.RetrieveUpdateDestroyAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    lookup_url_kwarg = 'gallery_image_id'


class AnalyticsBase(APIView):
    permission_classes = [IsAdminUser]

    def _safe_pct(self, current, previous):
        if previous == 0:
            return 100.0 if current > 0 else 0.0
        return round(((current - previous) / previous) * 100, 2)

    def _period_stats_dt(self, queryset, field_name, start, end):
        prev_start = start - (end - start)
        current = queryset.filter(**{f"{field_name}__gte": start, f"{field_name}__lt": end}).count()
        previous = queryset.filter(**{f"{field_name}__gte": prev_start, f"{field_name}__lt": start}).count()
        return {
            "current": current,
            "previous": previous,
            "change_pct": self._safe_pct(current, previous),
        }

    def _period_stats_date(self, queryset, field_name, start_date, end_date):
        prev_start_date = start_date - (end_date - start_date)
        current = queryset.filter(**{f"{field_name}__gte": start_date, f"{field_name}__lt": end_date}).count()
        previous = queryset.filter(**{f"{field_name}__gte": prev_start_date, f"{field_name}__lt": start_date}).count()
        return {
            "current": current,
            "previous": previous,
            "change_pct": self._safe_pct(current, previous),
        }

    def _daily_counts(self, queryset, field_name, start, end):
        rows = (
            queryset.filter(**{f"{field_name}__gte": start, f"{field_name}__lt": end})
            .annotate(day=TruncDate(field_name))
            .values("day")
            .annotate(count=Count("id"))
            .order_by("day")
        )
        return {row["day"].isoformat(): row["count"] for row in rows}

    def _get_period(self, request):
        try:
            period_days = int(request.query_params.get("days", 30))
        except ValueError:
            period_days = 30

        period_days = max(7, min(period_days, 365))

        now = timezone.now()
        start = now - timedelta(days=period_days - 1)
        end = now + timedelta(seconds=1)
        start_date = start.date()
        end_date = now.date() + timedelta(days=1)
        return {
            "period_days": period_days,
            "now": now,
            "start": start,
            "end": end,
            "start_date": start_date,
            "end_date": end_date,
        }

    def _overview(self):
        totals = {
            "sermons": Sermon.objects.count(),
            "series": Series.objects.count(),
            "events": Event.objects.count(),
            "devotions": Devotion.objects.count(),
            "reflections": Reflection.objects.count(),
            "prayer_requests": Prayer_request.objects.count(),
            "announcements": Announcement.objects.count(),
            "live_streams": Live_stream.objects.count(),
            "galleries": Gallery.objects.count(),
            "gallery_images": GalleryImage.objects.count(),
            "resources": Resource.objects.count(),
            "reels": Reel.objects.count(),
            "contribution_channels": ContributionChannel.objects.count(),
            "contribution_intents": ContributionIntent.objects.count(),
            "staff_users": get_user_model().objects.filter(is_staff=True).count(),
        }
        return totals

    def _growth(self, period):
        growth = {
            "sermons": self._period_stats_dt(Sermon.objects.all(), "date", period["start"], period["end"]),
            "series": self._period_stats_dt(Series.objects.all(), "date", period["start"], period["end"]),
            "events": self._period_stats_date(Event.objects.all(), "date", period["start_date"], period["end_date"]),
            "devotions": self._period_stats_dt(Devotion.objects.all(), "date", period["start"], period["end"]),
            "reflections": self._period_stats_dt(Reflection.objects.all(), "date", period["start"], period["end"]),
            "prayer_requests": self._period_stats_dt(Prayer_request.objects.all(), "date", period["start"], period["end"]),
            "gallery_images": self._period_stats_dt(GalleryImage.objects.all(), "date", period["start"], period["end"]),
            "reels": self._period_stats_dt(Reel.objects.all(), "created_at", period["start"], period["end"]),
            "contribution_intents": self._period_stats_dt(ContributionIntent.objects.all(), "created_at", period["start"], period["end"]),
        }
        return growth

    def _engagement(self, totals):
        sermon_likes = Sermon.objects.aggregate(v=Sum("likes"))["v"] or 0
        series_likes = Series.objects.aggregate(v=Sum("likes"))["v"] or 0
        reflection_likes = Reflection.objects.aggregate(v=Sum("likes"))["v"] or 0
        gallery_likes = Gallery.objects.aggregate(v=Sum("likes"))["v"] or 0
        gallery_image_likes = GalleryImage.objects.aggregate(v=Sum("likes"))["v"] or 0
        reel_likes = Reel.objects.aggregate(v=Sum("likes_count"))["v"] or 0
        live_reactions = Live_stream.objects.aggregate(v=Sum("reactions"))["v"] or 0

        comment_records = (
            Sermon.objects.exclude(comments__exact="").count()
            + Reflection.objects.exclude(comments__exact="").count()
            + Live_stream.objects.exclude(comments__exact="").count()
        )

        total_likes = sermon_likes + series_likes + reflection_likes + gallery_likes + gallery_image_likes + reel_likes
        total_reactions = total_likes + live_reactions  # kept for index computation
        content_base = max(
            totals["sermons"] + totals["series"] + totals["devotions"] + totals["reflections"] + totals["gallery_images"] + totals["reels"],
            1,
        )
        engagement_index = round(total_reactions / content_base, 2)
        return {
            "total_likes": total_likes,
            "live_reactions": live_reactions,
            "comment_records": comment_records,
            "engagement_index": engagement_index,
        }

    def _contributions(self, totals):
        contribution_totals = ContributionIntent.objects.aggregate(total_amount=Sum("amount"))
        # Compute status amounts via filtered querysets for broad compatibility.
        confirmed_amount = ContributionIntent.objects.filter(status="confirmed").aggregate(v=Sum("amount"))["v"] or 0
        pending_amount = ContributionIntent.objects.filter(status="pending").aggregate(v=Sum("amount"))["v"] or 0
        rejected_amount = ContributionIntent.objects.filter(status="rejected").aggregate(v=Sum("amount"))["v"] or 0

        contributions = {
            "intent_count": totals["contribution_intents"],
            "total_amount": contribution_totals["total_amount"] or 0,
            "confirmed_amount": confirmed_amount,
            "pending_amount": pending_amount,
            "rejected_amount": rejected_amount,
            "status_breakdown": {
                "pending": ContributionIntent.objects.filter(status="pending").count(),
                "confirmed": ContributionIntent.objects.filter(status="confirmed").count(),
                "rejected": ContributionIntent.objects.filter(status="rejected").count(),
            },
            "by_channel_type": list(
                ContributionIntent.objects.values("channel__channel_type")
                .annotate(count=Count("id"), amount=Sum("amount"))
                .order_by("channel__channel_type")
            ),
            "by_purpose": list(
                ContributionIntent.objects.values("purpose")
                .annotate(count=Count("id"), amount=Sum("amount"))
                .order_by("purpose")
            ),
        }
        return contributions

    def _upcoming(self, period):
        upcoming = {
            "events_next_30_days": Event.objects.filter(
                date__gte=period["now"].date(), date__lte=period["now"].date() + timedelta(days=30)
            ).count(),
            "live_streams_upcoming": Live_stream.objects.filter(status="upcoming").count(),
            "next_event": Event.objects.filter(date__gte=period["now"].date()).order_by("date").values(
                "id", "name", "date", "location"
            ).first(),
        }
        return upcoming

    def _top_content(self):
        top_content = {
            "sermons": list(Sermon.objects.order_by("-likes", "-date").values("id", "title", "likes")[:5]),
            "reels": list(Reel.objects.order_by("-views_count", "-likes_count").values(
                "id", "title", "views_count", "likes_count", "is_published"
            )[:5]),
            "gallery_images": list(GalleryImage.objects.order_by("-likes", "-date").values(
                "id", "title", "likes", "gallery__title"
            )[:5]),
        }
        return top_content

    def _timeline(self, period):
        dates = [(period["start"].date() + timedelta(days=i)).isoformat() for i in range(period["period_days"])]
        sermon_daily = self._daily_counts(Sermon.objects.all(), "date", period["start"], period["end"])
        devotion_daily = self._daily_counts(Devotion.objects.all(), "date", period["start"], period["end"])
        reflection_daily = self._daily_counts(Reflection.objects.all(), "date", period["start"], period["end"])
        contribution_daily = self._daily_counts(ContributionIntent.objects.all(), "created_at", period["start"], period["end"])
        reel_daily = self._daily_counts(Reel.objects.all(), "created_at", period["start"], period["end"])
        gallery_daily = self._daily_counts(GalleryImage.objects.all(), "date", period["start"], period["end"])

        timeline = []
        for day in dates:
            timeline.append({
                "day": day,
                "sermons": sermon_daily.get(day, 0),
                "devotions": devotion_daily.get(day, 0),
                "reflections": reflection_daily.get(day, 0),
                "contribution_intents": contribution_daily.get(day, 0),
                "reels": reel_daily.get(day, 0),
                "gallery_images": gallery_daily.get(day, 0),
            })
        return timeline

@extend_schema(tags=['Analytics'], description="Analytics endpoint index. Use dedicated endpoints for faster loads.")
class DashboardAnalytics(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "period_days": period["period_days"],
            "endpoints": {
                "overview": "/api/analytics/overview/",
                "growth": "/api/analytics/growth/?days=30",
                "engagement": "/api/analytics/engagement/",
                "contributions": "/api/analytics/contributions/",
                "upcoming": "/api/analytics/upcoming/",
                "top_content": "/api/analytics/top-content/",
                "timeline": "/api/analytics/timeline/?days=30",
            }
        })


@extend_schema(tags=['Analytics'], description="Top-level totals used for dashboard KPI cards.")
class AnalyticsOverview(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "overview": self._overview(),
        })


@extend_schema(tags=['Analytics'], description="Growth comparison between current and previous period.")
class AnalyticsGrowth(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "period_days": period["period_days"],
            "growth": self._growth(period),
        })


@extend_schema(tags=['Analytics'], description="Engagement metrics from reactions, likes, and comments.")
class AnalyticsEngagement(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        overview = self._overview()
        return Response({
            "generated_at": period["now"].isoformat(),
            "engagement": self._engagement(overview),
        })


@extend_schema(tags=['Analytics'], description="Contribution analytics breakdown by status, type, and purpose.")
class AnalyticsContributions(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        overview = self._overview()
        return Response({
            "generated_at": period["now"].isoformat(),
            "contributions": self._contributions(overview),
        })


@extend_schema(tags=['Analytics'], description="Upcoming operational insights (next events and streams).")
class AnalyticsUpcoming(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "upcoming": self._upcoming(period),
        })


@extend_schema(tags=['Analytics'], description="Top-performing content lists for dashboard highlights.")
class AnalyticsTopContent(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "top_content": self._top_content(),
        })


@extend_schema(tags=['Analytics'], description="Time-series dataset for dashboard charts.")
class AnalyticsTimeline(AnalyticsBase):
    def get(self, request):
        period = self._get_period(request)
        return Response({
            "generated_at": period["now"].isoformat(),
            "period_days": period["period_days"],
            "timeline": self._timeline(period),
        })
