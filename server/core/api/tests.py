from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import SiteSettings, ThemeSettings


class SiteConfigApiTests(APITestCase):
    def setUp(self):
        self.public_url = reverse('site-config-public')
        self.settings_url = reverse('site-settings')
        self.theme_url = reverse('theme-settings')

        User = get_user_model()
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='pass12345',
            is_staff=True,
            is_superuser=True,
        )
        self.member = User.objects.create_user(
            username='member',
            email='member@example.com',
            password='pass12345',
            is_staff=False,
            is_superuser=False,
        )

    def test_public_site_config_returns_defaults(self):
        response = self.client.get(self.public_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('site', response.data)
        self.assertIn('theme', response.data)
        self.assertIn('navigation', response.data)
        self.assertIn('pages', response.data)
        self.assertTrue(SiteSettings.objects.filter(pk=1).exists())
        self.assertTrue(ThemeSettings.objects.filter(pk=1).exists())

    def test_admin_can_update_site_settings(self):
        self.client.force_authenticate(self.admin)
        payload = {'church_name': 'Elevation Church HQ'}
        response = self.client.patch(self.settings_url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['church_name'], payload['church_name'])
        self.assertEqual(SiteSettings.load().church_name, payload['church_name'])

    def test_non_admin_cannot_update_theme(self):
        self.client.force_authenticate(self.member)
        response = self.client.patch(self.theme_url, {'primary_color': '#000000'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
