from django.urls import path

from dashboardapp import views

urlpatterns = [
    path('donations-by-category/', views.donations_by_category_view, name='donations_by_category'),
    path('average-donation-by-category/', views.average_donation_by_category_view, name='average_donation_by_category'),
    path('donations-per-project/', views.donations_per_project_view, name='donations_per_project'),
    path('followers-per-project/', views.followers_per_project_view, name='followers_per_project'),
    path('highest-goal-projects/', views.highest_goal_projects_view, name='highest_goal_projects'),
    path('project-status-distribution/', views.project_status_distribution_view, name='project_status_distribution'),

    path('dashboard/plotly/', views.dashboard_view_plotly, name='dashboard_plotly'),
    path('dashboard/plotly/filters/', views.dashboard_plotly_filters, name='dashboard_plotly_filters'),

    path("dashboard/bokeh/", views.dashboard_view_bokeh, name="dashboard_bokeh"),
    path("dashboard/bokeh/filters/", views.dashboard_bokeh_filters, name="dashboard_bokeh_filters"),

    path("analyze_model_attributes/", views.analyze_model_attributes, name="analyze_model_attributes"),
    path("get_attributes/", views.get_model_attributes, name="get_attributes"),
    path('performance-dashboard/', views.performance_dashboard, name='performance_dashboard'),
]
