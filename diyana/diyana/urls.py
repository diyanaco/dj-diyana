"""diyana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls.conf import re_path
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubtaskViewSet)
router.register(r'codes', views.CodeViewSet)
router.register(r'priorities', views.PriorityViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'phases', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('admin/', admin.site.urls),
]

urlpatterns.append(
    re_path(
        r"^tasks/(?P<pk>[^/.]+)/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.TaskViewSet.as_view({"get": "retrieve_related"}),
        name="task-related",
    ))

urlpatterns.append(
    re_path(
        r"^tasks/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.TaskRelationshipView.as_view(),
        name="task-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^subtasks/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z]+)*)$",
        views.SubtaskViewSet.as_view({"get": "retrieve_related"}),
        name="subtask-related",
    ))

urlpatterns.append(
    re_path(
        r"^subtasks/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z]+)*)$",
        views.SubtaskRelationshipView.as_view(),
        name="subtask-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^projects/(?P<pk>[^/.]+)/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.ProjectViewSet.as_view({"get": "retrieve_related"}),
        name="project-related",
    ))

urlpatterns.append(
    re_path(
        r"^projects/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.ProjectRelationshipView.as_view(),
        name="project-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^phases/(?P<pk>[^/.]+)/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.PhaseViewSet.as_view({"get": "retrieve_related"}),
        name="phase-related",
    ))

urlpatterns.append(
    re_path(
        r"^phases/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z]+(?:-[a-z_]+)*)$",
        views.PhaseRelationshipView.as_view(),
        name="phase-relationships",
    ))