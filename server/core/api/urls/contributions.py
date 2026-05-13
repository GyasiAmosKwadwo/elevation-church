from django.urls import path
from api import views

urlpatterns = [
    path('channels/', views.ListContributionChannel.as_view(), name='contribution-channel-list'),
    path('channels/<uuid:channel_id>/', views.DetailContributionChannel.as_view(), name='contribution-channel-detail'),
    path('channels/create/', views.CreateContributionChannel.as_view(), name='contribution-channel-create'),
    path('channels/<uuid:channel_id>/update/', views.UpdateContributionChannel.as_view(), name='contribution-channel-update'),

    path('intents/', views.ListContributionIntent.as_view(), name='contribution-intent-list'),
    path('intents/create/', views.CreateContributionIntent.as_view(), name='contribution-intent-create'),
    path('intents/<uuid:intent_id>/', views.DetailContributionIntent.as_view(), name='contribution-intent-detail'),
    path('intents/<uuid:intent_id>/update/', views.UpdateContributionIntent.as_view(), name='contribution-intent-update'),
]
