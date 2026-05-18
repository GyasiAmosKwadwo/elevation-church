from django.urls import path
from api import views

urlpatterns = [
    path('passage/', views.BiblePassageDetail.as_view(), name='bible-passage-detail'),
    path('search/', views.BiblePassageSearch.as_view(), name='bible-passage-search'),
]
