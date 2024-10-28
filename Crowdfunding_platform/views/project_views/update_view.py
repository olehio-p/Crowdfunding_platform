from django.utils import timezone

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.update_serializer import UpdateSerializer

class UpdateViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of updates",
        responses={
            200: UpdateSerializer(many=True),
        }
    )
    def list(self, request):
        with self.unitOfWork:
            updates = self.unitOfWork.updates.get_all()
        serializer = UpdateSerializer(updates, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve an update by ID",
        responses={
            200: UpdateSerializer,
            404: "Update not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            update = self.unitOfWork.updates.get(pk)
        if update is None:
            return Response({"error": "Update not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(update)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new update",
        request_body=UpdateSerializer,
        responses={
            201: UpdateSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                update = self.unitOfWork.updates.create(
                    project=serializer.validated_data.get('project'),
                    title=serializer.validated_data.get('title'),
                    content=serializer.validated_data.get('content'),
                    date=serializer.validated_data.get('date', timezone.now())
                )
            return Response(UpdateSerializer(update).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing update",
        request_body=UpdateSerializer,
        responses={
            200: UpdateSerializer,
            404: "Update not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            update = self.unitOfWork.updates.get(pk)
        if not update:
            return Response({"error": "Update not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(update, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_update = self.unitOfWork.updates.update(
                    pk,
                    project=serializer.validated_data.get('project', update.project),
                    title=serializer.validated_data.get('title', update.title),
                    content=serializer.validated_data.get('content', update.content),
                    date=serializer.validated_data.get('date', update.date)
                )
            return Response(UpdateSerializer(updated_update).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete an update by ID",
        responses={
            204: "Update deleted successfully",
            404: "Update not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.updates.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Update not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Retrieve updates for a specific project",
        responses={
            200: UpdateSerializer(many=True),
            404: "Project not found"
        }
    )
    def get_updates_for_project(self, request, project_id=None):
        with self.unitOfWork:
            updates = self.unitOfWork.updates.get_all_by_project(project_id)
        if not updates:
            return Response({"error": "No updates found for this project"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UpdateSerializer(updates, many=True)
        return Response(serializer.data)