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

    def list(self, request):
        with self.unitOfWork:
            languages = self.unitOfWork.languages.get_all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            language = self.unitOfWork.languages.get(pk)
        if language is None:
            return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

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

    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.languages.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)
