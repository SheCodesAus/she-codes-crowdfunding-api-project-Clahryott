from django.shortcuts import render
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.http import Http404
from django.db import IntegrityError

from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

# Create views here 
class ProjectList(APIView): #long code version for project (this is what is in the container, so to speak)

    def get(self, request): #using GET here // when you get a get request this is what you do
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True) 
        return Response(serializer.data) #means get the data out of serializer

    def post(self, request): #using a POST request here
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       

class ProjectDetail(APIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] #adding to view - only the project owner can edit

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk) #pk = the variable we give to the pk (primary key)
            self.check_object_permissions(self.request, project) # this is an additional layer for permission checks
            #return Project.objects.get(pk=pk)
            return project
        except Project.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(instance=project,data=data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PledgeList(generics.ListCreateAPIView): #this is a condensed version of the code written above, such as class projectlist
    
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

    def get(self, request):
        pledges = self.get_queryset()
        if not pledges:
            return Response({"message": "We need your help! Pick a project and send pledge to help us along"}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(pledges, many=True)
        return Response(serializer.data)
        
class PledgeDetailView(generics.RetrieveUpdateDestroyAPIView): #this is a condensed version of the code written above, such as class projectlist
    
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer