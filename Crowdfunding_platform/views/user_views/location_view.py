from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.user_serializers.location_serializer import LocationSerializer

class LocationViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of all locations",
        responses={200: LocationSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            locations = self.unitOfWork.locations.get_all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a location by ID",
        responses={
            200: LocationSerializer,
            404: "Location not found"
        },
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            location = self.unitOfWork.locations.get(pk)
        if location is None:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new location",
        request_body=LocationSerializer,
        responses={201: LocationSerializer, 400: "Invalid data"},
    )
    def create(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                location = self.unitOfWork.locations.create(
                    country=serializer.validated_data.get('country'),
                    state=serializer.validated_data.get('state'),
                    city=serializer.validated_data.get('city'),
                    postal_code=serializer.validated_data.get('postal_code')
                )
            return Response(LocationSerializer(location).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing location",
        request_body=LocationSerializer,
        responses={200: LocationSerializer, 404: "Location not found", 400: "Invalid data"},
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            location = self.unitOfWork.locations.get(pk)
        if not location:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = LocationSerializer(location, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_location = self.unitOfWork.locations.update(
                    pk,
                    country=serializer.validated_data.get('country', location.country),
                    state=serializer.validated_data.get('state', location.state),
                    city=serializer.validated_data.get('city', location.city),
                    postal_code=serializer.validated_data.get('postal_code', location.postal_code)
                )
            return Response(LocationSerializer(updated_location).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a location by ID",
        responses={204: "Location deleted successfully", 404: "Location not found"},
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.locations.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
