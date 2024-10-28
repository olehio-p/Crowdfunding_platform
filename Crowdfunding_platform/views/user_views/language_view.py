from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.user_serializers.language_serializer import LanguageSerializer

class LanguageViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of all languages",
        responses={200: LanguageSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            languages = self.unitOfWork.languages.get_all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a language by ID",
        responses={200: LanguageSerializer, 404: "Language not found"},
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            language = self.unitOfWork.languages.get(pk)
        if language is None:
            return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new language",
        request_body=LanguageSerializer,
        responses={201: LanguageSerializer, 400: "Invalid data"},
    )
    def create(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                language = self.unitOfWork.languages.create(
                    code=serializer.validated_data.get('code'),
                    name=serializer.validated_data.get('name')
                )
            return Response(LanguageSerializer(language).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing language",
        request_body=LanguageSerializer,
        responses={200: LanguageSerializer, 404: "Language not found", 400: "Invalid data"},
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            language = self.unitOfWork.languages.get(pk)
        if not language:
            return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_language = self.unitOfWork.languages.update(
                    pk,
                    code=serializer.validated_data.get('code', language.code),
                    name=serializer.validated_data.get('name', language.name)
                )
            return Response(LanguageSerializer(updated_language).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a language by ID",
        responses={204: "Language deleted successfully", 404: "Language not found"},
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.languages.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
