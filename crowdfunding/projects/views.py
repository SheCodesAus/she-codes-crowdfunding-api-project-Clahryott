from django.shortcuts import render  # doesnt appear to be working
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.exceptions import NotFound   ###
from django.http import Http404
# from django.db import IntegrityError #####  CHECK ?


from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .serializers import CustomUserSerializer
# IsSupporterOrReadOnly #do i need the last bit?
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly


# Create views here

# long code version for project (this is what is in the container, so to speak)
class ProjectList(APIView):

    # to add or not? ######
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request):  # using GET here // when you get a get request this is what you do /// auto adds userid as owner
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        # filter for open projects only
        is_open = request.query_params.get('is_open', None)
        if is_open:
            projects = projects.filter(is_open=is_open)
        # means get the data out of serializer
        return Response(serializer.data)

    def post(self, request):  # using a POST request here
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):

    # adding to view - only the project owner can edit
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            # pk = the variable we give to the pk (primary key)
            project = Project.objects.get(pk=pk)
            # this is an additional layer for permission checks
            self.check_object_permissions(self.request, project)
            # return Project.objects.get(pk=pk)
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
        serializer = ProjectDetailSerializer(
            instance=project, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# this is a condensed version of the code written above, such as class projectlist


class PledgeList(generics.ListCreateAPIView):

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

    def get(self, request):
        pledges = self.get_queryset()
        if not pledges:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(pledges, many=True)
        return Response(serializer.data)


# this is a condensed version, such as class projectlist
class PledgeDetailView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]

    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    # def perform_update(self, serializer):  ### ---- do i need this?
    #    instance = serializer.save(supporter=self.request.user)
    #    return instance
