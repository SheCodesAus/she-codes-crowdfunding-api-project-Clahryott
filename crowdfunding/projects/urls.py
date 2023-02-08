from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# models > serializers > views > urls(self) > crowdfunding urls

urlpatterns = [
    # the naming convention -- need to have / after projects and "name=project-list" is django standard
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    # path('projects/filter', views.ProjectListFilter.as_view(), name="project-list-filter"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetailView.as_view(), name='pledge-detail'),
]

# takes all your urls and lets you choose if you want json etc back
urlpatterns = format_suffix_patterns(urlpatterns)
