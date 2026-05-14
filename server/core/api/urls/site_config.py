from django.urls import path
from api import views

urlpatterns = [
    path('public/', views.PublicSiteConfiguration.as_view(), name='site-config-public'),
    path('settings/', views.RetrieveUpdateSiteSettings.as_view(), name='site-settings'),
    path('theme/', views.RetrieveUpdateThemeSettings.as_view(), name='theme-settings'),

    path('navigation/', views.ListCreateNavigationItem.as_view(), name='navigation-list'),
    path('navigation/<uuid:item_id>/', views.DetailUpdateNavigationItem.as_view(), name='navigation-detail'),

    path('pages/', views.ListCreatePageConfig.as_view(), name='page-config-list'),
    path('pages/<slug:slug>/', views.DetailUpdatePageConfig.as_view(), name='page-config-detail'),

    path('sections/', views.ListCreateSectionConfig.as_view(), name='section-config-list'),
    path('sections/<uuid:section_id>/', views.DetailUpdateSectionConfig.as_view(), name='section-config-detail'),
]
