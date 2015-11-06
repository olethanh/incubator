from django.conf.urls import patterns, url

from .views import ProjectDetailView, ProjectAddView, ProjectEditView

urlpatterns = patterns(
    '',
    url(r'^$', 'projects.views.projects_home', name='projects_home'),
    url(r'^add$', ProjectAddView.as_view(), name='add_project'),
    url(r'^edit/(?P<pk>[0-9]+)$', ProjectEditView.as_view(), name='edit_project'),
    url(r'^(?P<pk>[0-9]+)', ProjectDetailView.as_view(), name='view_project'),
    url(r'^partcipe/(?P<pk>[0-9]+)', 'projects.views.add_participation', name='project_add_participation'),
)
