from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

PROJECT_URL = reverse('tasks:project-list')

class PublicProjectAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(PROJECT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
