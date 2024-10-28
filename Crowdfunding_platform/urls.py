from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Crowdfunding_platform.views.auth_view import RegisterView, LoginView, LogoutView, UserDetailsView
from Crowdfunding_platform.views.project_views.category_view import CategoryViewSet
from Crowdfunding_platform.views.project_views.comment_view import CommentViewSet
from Crowdfunding_platform.views.project_views.follower_view import FollowerViewSet
from Crowdfunding_platform.views.project_views.milestone_view import MilestoneViewSet
from Crowdfunding_platform.views.project_views.project_view import ProjectViewSet
from Crowdfunding_platform.views.project_views.report_view import ReportViewSet
from Crowdfunding_platform.views.project_views.update_view import UpdateViewSet
from Crowdfunding_platform.views.user_views.custom_user_view import CustomUserViewSet
from Crowdfunding_platform.views.user_views.language_view import LanguageViewSet
from Crowdfunding_platform.views.user_views.location_view import LocationViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'updates', UpdateViewSet, basename='update')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'followers', FollowerViewSet, basename='follower')
router.register(r'milestones', MilestoneViewSet, basename='milestone')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'users', CustomUserViewSet, basename='user')

schema_view = get_schema_view(
    openapi.Info(
        title="Crowdfunding Platform API",
        default_version='v1',
        description="API documentation with Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/<int:project_id>/updates/', UpdateViewSet.as_view({'get': 'get_updates_for_project'}), name='project-updates'),
    path('api/projects/<int:project_id>/comments/', CommentViewSet.as_view({'get': 'get_comments_for_project'}), name='project-comments'),
    path('api/projects/<int:project_id>/followers/', CustomUserViewSet.as_view({'get': 'get_followers_for_project'}), name='project-followers'),
    path('api/projects/<int:project_id>/milestones/', MilestoneViewSet.as_view({'get': 'get_milestones_for_project'}), name='project-milestones'),
    path('api/projects/<int:project_id>/reports/', ReportViewSet.as_view({'get': 'get_reports_for_project'}), name='project-reports'),
    path('api/users/<int:user_id>/reports/', ReportViewSet.as_view({'get': 'get_reports_by_user'}), name='user-reports'),
    path('api/locations/<str:country>/users/', CustomUserViewSet.as_view({'get': 'get_users_by_country'}), name='country-users'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
