from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.user_serializers.custom_user_serializer import CustomUserSerializer


class CustomUserViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of all custom users",
        responses={200: CustomUserSerializer(many=True)}
    )
    def list(self, request):
        with self.unitOfWork:
            users = self.unitOfWork.custom_users.get_all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a custom user by ID",
        responses={200: CustomUserSerializer, 404: "Custom user not found"}
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            user = self.unitOfWork.custom_users.get(pk)
        if user is None:
            return Response({"error": "Custom user not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    # @swagger_auto_schema(
    #     operation_summary="Create a new custom user",
    #     request_body=CustomUserSerializer,
    #     responses={201: CustomUserSerializer, 400: "Invalid data"}
    # )
    # def create(self, request):
    #     serializer = CustomUserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         with self.unitOfWork:
    #             user_data = serializer.validated_data.get('user')
    #             user = User.objects.create(
    #                 username=user_data.get('username'),
    #                 email=user_data.get('email'),
    #                 first_name=user_data.get('first_name'),
    #                 last_name=user_data.get('last_name')
    #             )
    #             custom_user = self.unitOfWork.custom_users.create(
    #                 user=user,
    #                 profile_picture=serializer.validated_data.get('profile_picture'),
    #                 bio=serializer.validated_data.get('bio'),
    #                 user_type=serializer.validated_data.get('user_type'),
    #                 join_date=serializer.validated_data.get('join_date'),
    #                 phone_number=serializer.validated_data.get('phone_number'),
    #                 language=serializer.validated_data.get('language'),
    #                 location=serializer.validated_data.get('location')
    #             )
    #         return Response(CustomUserSerializer(custom_user).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing custom user",
        request_body=CustomUserSerializer,
        responses={200: CustomUserSerializer, 404: "Custom user not found", 400: "Invalid data"}
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            custom_user = self.unitOfWork.custom_users.get(pk)
        if not custom_user:
            return Response({"error": "Custom user not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CustomUserSerializer(custom_user, data=request.data, partial=True)

        if serializer.is_valid():
            with self.unitOfWork:
                user_data = serializer.validated_data.get('user')
                if user_data:
                    user = custom_user.user
                    user.username = user_data.get('username', user.username)
                    user.email = user_data.get('email', user.email)
                    user.first_name = user_data.get('first_name', user.first_name)
                    user.last_name = user_data.get('last_name', user.last_name)
                    user.save()

                updated_user = self.unitOfWork.custom_users.update(
                    pk,
                    profile_picture=serializer.validated_data.get('profile_picture', custom_user.profile_picture),
                    bio=serializer.validated_data.get('bio', custom_user.bio),
                    user_type=serializer.validated_data.get('user_type', custom_user.user_type),
                    join_date=serializer.validated_data.get('join_date', custom_user.join_date),
                    phone_number=serializer.validated_data.get('phone_number', custom_user.phone_number),
                    language=serializer.validated_data.get('language', custom_user.language),
                    location=serializer.validated_data.get('location', custom_user.location)
                )
            return Response(CustomUserSerializer(updated_user).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a custom user by ID",
        responses={204: "Custom user deleted successfully", 404: "Custom user not found"}
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.custom_users.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Custom user not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Retrieve users by country",
        responses={200: CustomUserSerializer(many=True)},
    )
    def get_users_by_country(self, request, country):
        with self.unitOfWork:
            users = self.unitOfWork.custom_users.get_all_by_country(country)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve followers for a specific project",
        responses={200: CustomUserSerializer(many=True)},
    )
    def get_followers_for_project(self, request, project_id=None):
        with self.unitOfWork:
            followers = self.unitOfWork.custom_users.get_users_by_project(project_id)
        serializer = CustomUserSerializer(followers, many=True)
        return Response(serializer.data)