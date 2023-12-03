from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from tasks.models import Project
from tasks.serializers import ProjectSerializer
import pprint

PROJECT_URL = reverse('project-list')


def create_project(groups, **params):
    """Create and return a sample recipe."""
    defaults = {
        'name': 'Diyana NLP project',
        'description':
        "Creating the first LLM with zero to no coding experience",
    }
    defaults.update(params)

    project = Project.objects.create(**defaults)
    project.groups.set([groups])
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
        self.factory = APIRequestFactory()
        self.group = create_group(name='Test Group One')
        self.group_2 = create_group(name='Test Group Two')
        self.user = create_user(email="user@test.com", password="testpass")
        self.user.groups.set([self.group])
        self.client.force_authenticate(self.user)

    def test_create_project(self):
        """Test creating a new project."""
        payload = {
            "data": {
                "type": "Project",
                "id": None,
                "attributes": {
                    "name": "TESTPROJECT",
                    "description": "This is a test a project",
                    "code": "TESTPROJECT_CODE"
                },
                "relationships": {
                    "groups": {
                        "data": [{
                            "type": "Group",
                            "id": self.group.id
                        }]
                    }
                }
            }
        }
        payload_attributes = payload['data']['attributes']
        payload_relationships_groups_data = payload['data']['relationships'][
            'groups']['data']

        res = self.client.post(path=PROJECT_URL, data=payload)
        project = Project.objects.get(id=res.data['id'])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        for key in payload_attributes.keys():
            self.assertEqual(payload_attributes[key], getattr(project, key))
        for group in payload_relationships_groups_data:
            self.assertEqual(
                group['id'],
                getattr(project.groups.filter(id=group['id'])[0], 'id'))

    def test_retrieve_projects(self):
        """Test retrieving projects."""
        create_project(groups=self.group,
                       name="Test Project 1",
                       code="TESTPROJECT1")
        create_project(groups=self.group,
                       name="Test Project 2",
                       code="TESTPROJECT2")
        create_project(groups=self.group,
                       name="Test Project 3",
                       code="TESTPROJECT3")

        res = self.client.get(PROJECT_URL)
        pprint.pprint(res.data)
        # request = self.factory.get(PROJECT_URL)
        projects = Project.objects.all()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), 3)

    def test_retrieve_projects_limited_to_group(self):
        """Test retrieving projects for group."""
        create_project(groups=self.group,
                       name="Test Project 1",
                       code="TESTPROJECT1")
        create_project(groups=self.group,
                       name="Test Project 2",
                       code="TESTPROJECT2")
        create_project(groups=self.group_2,
                       name="Test Project 3",
                       code="TESTPROJECT3")

        res = self.client.get(PROJECT_URL, {'groups': 1},)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)
        self.assertEqual(res.data[0]['name'], "Test Project 1")
