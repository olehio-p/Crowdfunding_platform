from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from Crowdfunding_platform.models.user_models.CustomUser import CustomUser
from Crowdfunding_platform.serializers.user_serializers.custom_user_serializer import CustomUserSerializer
from Crowdfunding_platform.serializers.user_serializers.user_login_serializer import UserLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    schema = None

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        join_date = request.data.get('join_date')

        if not join_date:
            join_date = timezone.now().strftime("%Y-%m-%d")
        else:
            parsed_join_date = parse_date(join_date)
            if parsed_join_date is None:
                return Response(
                    {"join_date": ["Date has wrong format. Use YYYY-MM-DD."]},
                    status=status.HTTP_400_BAD_REQUEST
                )
            join_date = parsed_join_date


        user_data = {
            'username': request.data.get('user.username'),
            'password': request.data.get('user.password'),
            'email': request.data.get('user.email'),
            'first_name': request.data.get('user.first_name'),
            'last_name': request.data.get('user.last_name')
        }

        custom_user_data = {
            'user': user_data,
            'profile_picture': request.data.get('profile_picture'),
            'bio': request.data.get('bio'),
            'user_type': request.data.get('user_type'),
            'join_date': join_date,
            'phone_number': request.data.get('phone_number'),
            'language': request.data.get('language'),
            'location': request.data.get('location')
        }

        custom_user_serializer = self.get_serializer(data=custom_user_data)
        custom_user_serializer.is_valid(raise_exception=True)

        self.perform_create(custom_user_serializer)

        return Response(custom_user_serializer.data, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    schema = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    schema = None

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        OutstandingToken.objects.filter(user=request.user).delete()
        BlacklistedToken.objects.create(token=token)
        logout(request)
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)


class UserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    schema = None

    def get_object(self):
        return self.request.user
