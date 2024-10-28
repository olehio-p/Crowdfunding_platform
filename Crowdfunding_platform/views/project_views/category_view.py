from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.category_serializer import CategorySerializer

class CategoryViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of categories",
        responses={
            200: CategorySerializer(many=True),
        }
    )
    def list(self, request):
        with self.unitOfWork:
            categories = self.unitOfWork.categories.get_all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a category by ID",
        responses={
            200: CategorySerializer,
            404: "Category not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            category = self.unitOfWork.categories.get(pk)
        if category is None:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new category",
        request_body=CategorySerializer,
        responses={
            201: CategorySerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                category = self.unitOfWork.categories.create(
                    name=serializer.validated_data.get('name'),
                    description=serializer.validated_data.get('description')
                )
            return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing category",
        request_body=CategorySerializer,
        responses={
            200: CategorySerializer,
            404: "Category not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            category = self.unitOfWork.categories.get(pk)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_category = self.unitOfWork.categories.update(
                    pk,
                    name=serializer.validated_data.get('name'),
                    description=serializer.validated_data.get('description')
                )
            return Response(CategorySerializer(updated_category).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a category by ID",
        responses={
            204: "Category deleted successfully",
            404: "Category not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.categories.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
