from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.milestone_serializer import MilestoneSerializer

class MilestoneViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of milestones",
        responses={200: MilestoneSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            milestones = self.unitOfWork.milestones.get_all()
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a milestone by ID",
        responses={
            200: MilestoneSerializer,
            404: "Milestone not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            milestone = self.unitOfWork.milestones.get(pk)
        if milestone is None:
            return Response({"error": "Milestone not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MilestoneSerializer(milestone)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new milestone",
        request_body=MilestoneSerializer,
        responses={
            201: MilestoneSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = MilestoneSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                milestone = self.unitOfWork.milestones.create(
                    project=serializer.validated_data['project'],
                    title=serializer.validated_data['title'],
                    description=serializer.validated_data.get('description'),
                    goal=serializer.validated_data['goal'],
                    completion_date=serializer.validated_data.get('completion_date')
                )
            return Response(MilestoneSerializer(milestone).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing milestone",
        request_body=MilestoneSerializer,
        responses={
            200: MilestoneSerializer,
            404: "Milestone not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            milestone = self.unitOfWork.milestones.get(pk)
        if not milestone:
            return Response({"error": "Milestone not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MilestoneSerializer(milestone, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_milestone = self.unitOfWork.milestones.update(
                    pk,
                    project=serializer.validated_data.get('project', milestone.project),
                    title=serializer.validated_data.get('title', milestone.title),
                    description=serializer.validated_data.get('description', milestone.description),
                    goal=serializer.validated_data.get('goal', milestone.goal),
                    completion_date=serializer.validated_data.get('completion_date', milestone.completion_date)
                )
            return Response(MilestoneSerializer(updated_milestone).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a milestone by ID",
        responses={
            204: "Milestone deleted successfully",
            404: "Milestone not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.milestones.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Milestone not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Retrieve milestones for a specific project",
        responses={200: MilestoneSerializer(many=True)},
    )
    def get_milestones_for_project(self, request, project_id=None):
        with self.unitOfWork:
            milestones = self.unitOfWork.milestones.get_all_by_project(project_id)
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)
