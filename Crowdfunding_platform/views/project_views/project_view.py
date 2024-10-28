from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.project_serializer import ProjectSerializer

class ProjectViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of projects",
        responses={
            200: ProjectSerializer(many=True),
        }
    )
    def list(self, request):
        with self.unitOfWork:
            projects = self.unitOfWork.projects.get_all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a project by ID",
        responses={
            200: ProjectSerializer,
            404: "Project not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            project = self.unitOfWork.projects.get(pk)
        if project is None:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new project",
        request_body=ProjectSerializer,
        responses={
            201: ProjectSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                project = self.unitOfWork.projects.create(
                    title=serializer.validated_data.get('title'),
                    description=serializer.validated_data.get('description'),
                    goal_amount=serializer.validated_data.get('goal_amount'),
                    current_amount=serializer.validated_data.get('current_amount'),
                    start_date=serializer.validated_data.get('start_date'),
                    end_date=serializer.validated_data.get('end_date'),
                    category=serializer.validated_data.get('category'),
                    status=serializer.validated_data.get('status'),
                    project_image=serializer.validated_data.get('project_image'),
                    tags=serializer.validated_data.get('tags'),
                    video_url=serializer.validated_data.get('video_url')
                )
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing project",
        request_body=ProjectSerializer,
        responses={
            200: ProjectSerializer,
            404: "Project not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            project = self.unitOfWork.projects.get(pk)
        if not project:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_project = self.unitOfWork.projects.update(
                    pk,
                    title=serializer.validated_data.get('title', project.title),
                    description=serializer.validated_data.get('description', project.description),
                    goal_amount=serializer.validated_data.get('goal_amount', project.goal_amount),
                    current_amount=serializer.validated_data.get('current_amount', project.current_amount),
                    start_date=serializer.validated_data.get('start_date', project.start_date),
                    end_date=serializer.validated_data.get('end_date', project.end_date),
                    category=serializer.validated_data.get('category', project.category),
                    status=serializer.validated_data.get('status', project.status),
                    project_image=serializer.validated_data.get('project_image', project.project_image),
                    tags=serializer.validated_data.get('tags', project.tags),
                    video_url=serializer.validated_data.get('video_url', project.video_url)
                )
            return Response(ProjectSerializer(updated_project).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a project by ID",
        responses={
            204: "Project deleted successfully",
            404: "Project not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.projects.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
