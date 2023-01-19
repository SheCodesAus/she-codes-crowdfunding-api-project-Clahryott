from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# models > serializers > views > urls(self) > crowdfunding urls 

urlpatterns = [
	path('projects/', views.ProjectList.as_view(), name='project-list'), #the naming convention
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
    path('pledges/', views.PledgeList.as_view(), name='pledge-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
