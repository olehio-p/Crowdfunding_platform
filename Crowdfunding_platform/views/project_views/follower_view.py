from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.follower_serializer import FollowerSerializer

class FollowerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of followers",
        responses={200: FollowerSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            followers = self.unitOfWork.followers.get_all()
        serializer = FollowerSerializer(followers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a follower by ID",
        responses={
            200: FollowerSerializer,
            404: "Follower not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            follower = self.unitOfWork.followers.get(pk)
        if follower is None:
            return Response({"error": "Follower not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FollowerSerializer(follower)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new follower",
        request_body=FollowerSerializer,
        responses={
            201: FollowerSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = FollowerSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                follower = self.unitOfWork.followers.create(
                    user=serializer.validated_data['user'],
                    project=serializer.validated_data['project']
                )
            return Response(FollowerSerializer(follower).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing follower",
        request_body=FollowerSerializer,
        responses={
            200: FollowerSerializer,
            404: "Follower not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            follower = self.unitOfWork.followers.get(pk)
        if not follower:
            return Response({"error": "Follower not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FollowerSerializer(follower, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_follower = self.unitOfWork.followers.update(
                    pk,
                    user=serializer.validated_data.get('user', follower.user),
                    project=serializer.validated_data.get('project', follower.project),
                )
            return Response(FollowerSerializer(updated_follower).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a follower by ID",
        responses={
            204: "Follower deleted successfully",
            404: "Follower not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.followers.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Follower not found"}, status=status.HTTP_404_NOT_FOUND)
