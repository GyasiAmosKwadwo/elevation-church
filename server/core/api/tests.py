from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Gallery, GalleryImage, SiteSettings, ThemeSettings


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


class GalleryApiTests(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.admin = User.objects.create_user(
            username='gallery_admin',
            email='gallery-admin@example.com',
            password='pass12345',
            is_staff=True,
            is_superuser=True,
        )
        self.create_url = reverse('gallery-create')

    def test_gallery_update_replaces_image_set_without_duplication(self):
        self.client.force_authenticate(self.admin)
        create_payload = {
            'title': 'Easter Service',
            'description': 'Initial description',
            'venue': 'Main Hall',
            'image_urls': [
                'https://example.com/image-1.jpg',
                'https://example.com/image-2.jpg',
                'https://example.com/image-3.jpg',
            ],
        }
        create_response = self.client.post(self.create_url, create_payload, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        gallery_id = create_response.data['id']
        update_url = reverse('gallery-update', kwargs={'gallery_id': gallery_id})
        update_payload = {
            'title': 'Easter Service Updated',
            'description': 'Updated description',
            'venue': 'Overflow Hall',
            'image_urls': [
                'https://example.com/image-1.jpg',
                'https://example.com/image-3.jpg',
            ],
        }
        update_response = self.client.patch(update_url, update_payload, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        gallery = Gallery.objects.get(pk=gallery_id)
        images = list(gallery.images.order_by('title'))
        self.assertEqual(len(images), 2)
        self.assertEqual(
            sorted(image.image for image in images),
            ['https://example.com/image-1.jpg', 'https://example.com/image-3.jpg'],
        )
        self.assertEqual(gallery.images.values_list('image', flat=True).distinct().count(), 2)
        for image in images:
            self.assertEqual(image.description, 'Updated description')
            self.assertEqual(image.venue, 'Overflow Hall')

    def test_gallery_update_without_image_urls_keeps_existing_images(self):
        self.client.force_authenticate(self.admin)
        create_payload = {
            'title': 'Sunday Highlights',
            'description': 'Gallery description',
            'venue': 'Church Grounds',
            'image_urls': [
                'https://example.com/highlight-1.jpg',
                'https://example.com/highlight-2.jpg',
            ],
        }
        create_response = self.client.post(self.create_url, create_payload, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        gallery_id = create_response.data['id']
        initial_images = sorted(
            GalleryImage.objects.filter(gallery_id=gallery_id).values_list('image', flat=True)
        )
        update_url = reverse('gallery-update', kwargs={'gallery_id': gallery_id})
        update_response = self.client.patch(update_url, {'title': 'Sunday Highlights v2'}, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)

        updated_images = sorted(
            GalleryImage.objects.filter(gallery_id=gallery_id).values_list('image', flat=True)
        )
        self.assertEqual(initial_images, updated_images)
