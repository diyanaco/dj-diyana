from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APIClient
from tasks.models import Project
from tasks.serializers import ProjectSerializer

PROJECT_URL = reverse('tasks:project-list')

def create_project(groups, **params):
    """Create and return a sample recipe."""
    defaults = {
        'name': 'Diyana NLP project',
        'description': "Creating the first LLM with zero to no coding experience",
    }
    defaults.update(params)

    project = Project.objects.create(groups=groups, **defaults)
    return project

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new user."""
    return Group.objects.create(**params)

class PublicProjectAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(PROJECT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.group = create_group(name='Test Group One')
        self.user = create_user(email="user@test.com", password="testpass")
        self.user.groups.set([self.group])
        self.client.force_authenticate(self.user)

    def test_create_project(self):
        """Test creating a new project."""
        payload = {
            'name': 'Test Project',
            'description': 'Test Project Description',
            'groups': self.group.id,
        }
        res = self.client.post(PROJECT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        project = Project.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(project, key))

    def test_retrieve_projects(self):
        """Test retrieving projects."""
        create_project(group=self.group, name="Test Project 1")
        create_project(group=self.group, name="Test Project 2")

        res = self.client.get(PROJECT_URL)
        projects = Project.objects.all().order_by('-name')
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_projects_limited_to_group(self):
        """Test retrieving projects for group."""
        group2 = create_group(name='Test Group 2')
        create_project(group=group2, name="Test Project 1")
        project = create_project(group=self.group, name="Test Project 2")

        res = self.client.get(PROJECT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], project.name)
