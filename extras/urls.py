from django.urls import path

from utils.views import ObjectChangeLog

from . import models, views

app_name = "extras"

urlpatterns = [
    # Config contexts
    path(
        "extras/config-contexts/",
        views.ConfigContextListView.as_view(),
        name="configcontext_list",
    ),
    path(
        "extras/config-contexts/add/",
        views.ConfigContextAdd.as_view(),
        name="configcontext_add",
    ),
    path(
        "config-contexts/<int:pk>/",
        views.ConfigContextView.as_view(),
        name="configcontext_view",
    ),
    path(
        "extras/config-contexts/<int:pk>/edit/",
        views.ConfigContextEditView.as_view(),
        name="configcontext_edit",
    ),
    path(
        "extras/config-contexts/delete/",
        views.ConfigContextBulkDeleteView.as_view(),
        name="configcontext_bulk_delete",
    ),
    path(
        "extras/config-contexts/<int:pk>/delete/",
        views.ConfigContextDeleteView.as_view(),
        name="configcontext_delete",
    ),
    path(
        "extras/config-contexts/<int:pk>/changelog/",
        ObjectChangeLog.as_view(),
        name="configcontext_changelog",
        kwargs={"model": models.ConfigContext},
    ),
    # Config context assignments
    path(
        "extras/config-context-assignments/add/",
        views.ConfigContextAssignmentEditView.as_view(),
        name="configcontextassignment_add",
    ),
    path(
        "extras/config-context-assignments/<int:pk>/edit/",
        views.ConfigContextAssignmentEditView.as_view(),
        name="configcontextassignment_edit",
    ),
    path(
        "extras/config-context-assignments/<int:pk>/delete/",
        views.ConfigContextAssignmentDeleteView.as_view(),
        name="configcontextassignment_delete",
    ),
    # IX-API
    path("ix-api/", views.IXAPIListView.as_view(), name="ixapi_list"),
    path("ix-api/add/", views.IXAPIAddView.as_view(), name="ixapi_add"),
    path("ix-api/<int:pk>/", views.IXAPIView.as_view(), name="ixapi_view"),
    path("ix-api/<int:pk>/edit/", views.IXAPIEditView.as_view(), name="ixapi_edit"),
    path(
        "ix-api/<int:pk>/delete/", views.IXAPIDeleteView.as_view(), name="ixapi_delete"
    ),
    path(
        "ix-api/<int:pk>/changelog/",
        ObjectChangeLog.as_view(),
        name="ixapi_changelog",
        kwargs={"model": models.IXAPI},
    ),
    # Job results
    path("job-results/", views.JobResultListView.as_view(), name="jobresult_list"),
    path("job-results/<int:pk>/", views.JobResultView.as_view(), name="jobresult_view"),
    path(
        "job-results/delete/",
        views.JobResultBulkDeleteView.as_view(),
        name="jobresult_bulk_delete",
    ),
    path(
        "job-results/<int:pk>/delete/",
        views.JobResultDeleteView.as_view(),
        name="jobresult_delete",
    ),
]
