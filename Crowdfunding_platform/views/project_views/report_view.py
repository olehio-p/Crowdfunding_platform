from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.report_serializer import ReportSerializer

class ReportViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of reports",
        responses={200: ReportSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            reports = self.unitOfWork.reports.get_all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a report by ID",
        responses={
            200: ReportSerializer,
            404: "Report not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            report = self.unitOfWork.reports.get(pk)
        if report is None:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new report",
        request_body=ReportSerializer,
        responses={
            201: ReportSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                report = self.unitOfWork.reports.create(
                    reported_by=serializer.validated_data.get('reported_by'),
                    project=serializer.validated_data.get('project'),
                    reason=serializer.validated_data.get('reason'),
                    date=serializer.validated_data.get('date', timezone.now()),
                    report_status=serializer.validated_data.get('report_status', 'pending')
                )
            return Response(ReportSerializer(report).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing report",
        request_body=ReportSerializer,
        responses={
            200: ReportSerializer,
            404: "Report not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            report = self.unitOfWork.reports.get(pk)
        if not report:
            return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReportSerializer(report, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_report = self.unitOfWork.reports.update(
                    pk,
                    reported_by=serializer.validated_data.get('reported_by', report.reported_by),
                    project=serializer.validated_data.get('project', report.project),
                    reason=serializer.validated_data.get('reason', report.reason),
                    date=serializer.validated_data.get('date', report.date),
                    report_status=serializer.validated_data.get('report_status', report.report_status)
                )
            return Response(ReportSerializer(updated_report).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a report by ID",
        responses={
            204: "Report deleted successfully",
            404: "Report not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.reports.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Report not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Retrieve reports for a specific project",
        responses={200: ReportSerializer(many=True)},
    )
    def get_reports_for_project(self, request, project_id=None):
        with self.unitOfWork:
            reports = self.unitOfWork.reports.get_all_by_project(project_id)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve reports by a specific user",
        responses={200: ReportSerializer(many=True)},
    )
    def get_reports_by_user(self, request, user_id=None):
        with self.unitOfWork:
            reports = self.unitOfWork.reports.get_all_by_user(user_id)
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)