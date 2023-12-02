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

app_name = 'tasks'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'templates', views.TemplateViewSet)
router.register(r'phases', views.PhaseViewSet)
router.register(r'grouptasks', views.GroupTaskViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'subtasks', views.SubtaskViewSet)
# router.register(r'codes', views.CodeViewSet)
router.register(r'priorities', views.PriorityViewSet)
router.register(r'milestones', views.MilestoneViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'dates', views.DateDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),

]

urlpatterns.append(
    re_path(
        r"^tasks/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.TaskViewSet.as_view({"get": "retrieve_related"}),
        name="task-related",
    ))

urlpatterns.append(
    re_path(
        r"^tasks/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
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
        r"^projects/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.ProjectViewSet.as_view({"get": "retrieve_related"}),
        name="project-related",
    ))

urlpatterns.append(
    re_path(
        r"^projects/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.ProjectRelationshipView.as_view(),
        name="project-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^phases/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.PhaseViewSet.as_view({"get": "retrieve_related"}),
        name="phase-related",
    ))

urlpatterns.append(
    re_path(
        r"^phases/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.PhaseRelationshipView.as_view(),
        name="phase-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^milestones/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.MilestoneViewSet.as_view({"get": "retrieve_related"}),
        name="milestone-related",
    ))

urlpatterns.append(
    re_path(
        r"^milestones/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.MilestoneRelationshipView.as_view(),
        name="milestone-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^grouptasks/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.GroupTaskViewSet.as_view({"get": "retrieve_related"}),
        name="grouptask-related",
    ))

urlpatterns.append(
    re_path(
        r"^grouptasks/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.GroupTaskRelationshipView.as_view(),
        name="grouptask-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^tags/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.TagViewSet.as_view({"get": "retrieve_related"}),
        name="tag-related",
    ))

urlpatterns.append(
    re_path(
        r"^tags/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.TagRelationshipView.as_view(),
        name="tag-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^templates/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.TemplateViewSet.as_view({"get": "retrieve_related"}),
        name="template-related",
    ))

urlpatterns.append(
    re_path(
        r"^templates/(?P<pk>[^/.]+)/relationships/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.TemplateRelationshipView.as_view(),
        name="template-relationships",
    ))

urlpatterns.append(
    re_path(
        r"^dates/(?P<pk>[^/.]+)/(?P<related_field>[a-z_]+(?:-[a-z_]+)*)$",
        views.DateDetailViewSet.as_view({"get": "retrieve_related"}),
        name="dates-related",
    ))
