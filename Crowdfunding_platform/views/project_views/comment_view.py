from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from Crowdfunding_platform.repositories.unit_of_work import DjangoUnitOfWork
from Crowdfunding_platform.serializers.project_serializers.comment_serializer import CommentSerializer

class CommentViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unitOfWork = DjangoUnitOfWork()

    @swagger_auto_schema(
        operation_summary="Retrieve a list of comments",
        responses={200: CommentSerializer(many=True)},
    )
    def list(self, request):
        with self.unitOfWork:
            comments = self.unitOfWork.comments.get_all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Retrieve a comment by ID",
        responses={
            200: CommentSerializer,
            404: "Comment not found"
        }
    )
    def retrieve(self, request, pk=None):
        with self.unitOfWork:
            comment = self.unitOfWork.comments.get(pk)
        if comment is None:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new comment",
        request_body=CommentSerializer,
        responses={
            201: CommentSerializer,
            400: "Invalid data"
        }
    )
    def create(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            with self.unitOfWork:
                comment = self.unitOfWork.comments.create(
                    project=serializer.validated_data.get('project'),
                    user=serializer.validated_data.get('user'),
                    text=serializer.validated_data.get('text')
                )
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update an existing comment",
        request_body=CommentSerializer,
        responses={
            200: CommentSerializer,
            404: "Comment not found",
            400: "Invalid data"
        }
    )
    def update(self, request, pk=None):
        with self.unitOfWork:
            comment = self.unitOfWork.comments.get(pk)
        if not comment:
            return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            with self.unitOfWork:
                updated_comment = self.unitOfWork.comments.update(
                    pk,
                    project=serializer.validated_data.get('project', comment.project),
                    user=serializer.validated_data.get('user', comment.user),
                    text=serializer.validated_data.get('text', comment.text)
                )
            return Response(CommentSerializer(updated_comment).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a comment by ID",
        responses={
            204: "Comment deleted successfully",
            404: "Comment not found"
        }
    )
    def destroy(self, request, pk=None):
        with self.unitOfWork:
            if self.unitOfWork.comments.delete(pk):
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Retrieve comments for a specific project",
        responses={200: CommentSerializer(many=True)},
    )
    def get_comments_for_project(self, request, project_id=None):
        with self.unitOfWork:
            comments = self.unitOfWork.comments.get_all_by_project(project_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
