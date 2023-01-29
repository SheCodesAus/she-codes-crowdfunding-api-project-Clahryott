from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# models > serializers > views > urls(self) > crowdfunding urls 

urlpatterns = [
	path('projects/', views.ProjectList.as_view(), name='project-list'), #the naming convention -- need to have / after projects and "name=project-list" is django standard
    #path('projects/filter', views.ProjectListFilter.as_view(), name="project-list-filter"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list'),
    path('pledges/<int:pk>/', views.PledgeDetailView.as_view(), name='pledge-detail') ##########
]

urlpatterns = format_suffix_patterns(urlpatterns) #takes all your urls and lets you choose if you want json etc back
