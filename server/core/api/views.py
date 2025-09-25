from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Sermon, Resource, Series, Event
from .serializers import SermonSerializer, ResourceSerializer, SeriesSerializer, EventSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination




class ListSermon(generics.ListAPIView):
    queryset = Sermon.objects.all()
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
    queryset = Resource.objects.all()
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
    queryset = Series.objects.all()
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
    queryset = Event.objects.all()
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

