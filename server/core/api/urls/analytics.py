from django.urls import path
from api import views

urlpatterns = [
    path('dashboard/', views.DashboardAnalytics.as_view(), name='analytics-dashboard'),
    path('overview/', views.AnalyticsOverview.as_view(), name='analytics-overview'),
    path('growth/', views.AnalyticsGrowth.as_view(), name='analytics-growth'),
    path('engagement/', views.AnalyticsEngagement.as_view(), name='analytics-engagement'),
    path('contributions/', views.AnalyticsContributions.as_view(), name='analytics-contributions'),
    path('upcoming/', views.AnalyticsUpcoming.as_view(), name='analytics-upcoming'),
    path('top-content/', views.AnalyticsTopContent.as_view(), name='analytics-top-content'),
    path('timeline/', views.AnalyticsTimeline.as_view(), name='analytics-timeline'),
]
