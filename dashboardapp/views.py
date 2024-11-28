import json
import os

from django.shortcuts import render
from django.http import JsonResponse

from Crowdfunding_platform import settings
from Crowdfunding_platform.models.project_models.Category import Category
from .db_performance import run_crowdfunding_tests
from .forms import ModelAttributeForm
from Crowdfunding_platform.repositories.project_repository import ProjectRepository
from dashboardapp.dashboards.plotly_dashboard import *
from dashboardapp.dashboards.bokeh_dashboard import *

project_repository = ProjectRepository()

def dashboard_bokeh_filters(request):
    category = request.GET.get('category', 'all')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    projects = project_repository.get_all_projects(
        category=category,
        start_date=start_date,
        end_date=end_date
    )

    bokeh_graphs = [
        bokeh_donations_by_category(
            project_repository.convert_decimal_to_float(
                project_repository.get_donations_by_category(projects)
            )
        ),
        bokeh_average_donation_by_category(
            project_repository.convert_decimal_to_float(
                project_repository.get_average_donation_by_category(projects)
            )
        ),
        bokeh_donations_per_project(
            project_repository.convert_decimal_to_float(
                project_repository.get_donations_per_project(projects)
            )
        ),
        bokeh_followers_per_project(
            project_repository.convert_decimal_to_float(
                project_repository.get_followers_per_project(projects)
            )
        ),
        bokeh_highest_goal_projects(
            project_repository.convert_decimal_to_float(
                project_repository.get_highest_goal_projects(projects)
            )
        ),
        bokeh_project_status_distribution(
            project_repository.get_project_status_distribution(projects)
        ),
    ]

    graphs_html = ''.join([div + script for div, script in bokeh_graphs])
    return JsonResponse({'graphs_html': graphs_html})


def dashboard_plotly_filters(request):
    category = request.GET.get('category', 'all')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    projects = project_repository.get_all_projects(
        category=category,
        start_date=start_date,
        end_date=end_date
    )

    plotly_graphs = [
        plotly_donations_by_category(
            project_repository.get_donations_by_category(projects)
        ),
        plotly_average_donation_by_category(
            project_repository.get_average_donation_by_category(projects)
        ),
        plotly_donations_per_project(
            project_repository.get_donations_per_project(projects)
        ),
        plotly_followers_per_project(
            project_repository.get_followers_per_project(projects)
        ),
        plotly_highest_goal_projects(
            project_repository.get_highest_goal_projects(projects)
        ),
        plotly_project_status_distribution(
            project_repository.get_project_status_distribution(projects)
        ),
    ]

    return JsonResponse({'graphs_html': plotly_graphs})


def dashboard_view_plotly(request):
    projects = project_repository.get_all_projects()

    graphs = [
        plotly_donations_by_category(
            project_repository.get_donations_by_category(projects)
        ),
        plotly_average_donation_by_category(
            project_repository.get_average_donation_by_category(projects)
        ),
        plotly_donations_per_project(
            project_repository.get_donations_per_project(projects)
        ),
        plotly_followers_per_project(
            project_repository.get_followers_per_project(projects)
        ),
        plotly_highest_goal_projects(
            project_repository.get_highest_goal_projects(projects)
        ),
        plotly_project_status_distribution(
            project_repository.get_project_status_distribution(projects)
        ),
    ]

    return render(request, "dashboard_plotly.html", {
        "plotly_graphs": graphs,
        "categories_data": Category.objects.values_list("name", "description"),
    })


def dashboard_view_bokeh(request):
    projects = project_repository.get_all_projects()

    bokeh_graphs = [
        bokeh_donations_by_category(
            project_repository.convert_decimal_to_float(
                project_repository.get_donations_by_category(projects)
            )
        ),
        bokeh_average_donation_by_category(
            project_repository.convert_decimal_to_float(
                project_repository.get_average_donation_by_category(projects)
            )
        ),
        bokeh_donations_per_project(
            project_repository.convert_decimal_to_float(
                project_repository.get_donations_per_project(projects)
            )
        ),
        bokeh_followers_per_project(
            project_repository.convert_decimal_to_float(
                project_repository.get_followers_per_project(projects)
            )
        ),
        bokeh_highest_goal_projects(
            project_repository.convert_decimal_to_float(
                project_repository.get_highest_goal_projects(projects)
            )
        ),
        bokeh_project_status_distribution(
            project_repository.get_project_status_distribution(projects)
        ),
    ]

    graphs_html = ''.join([div + script for div, script in bokeh_graphs])

    return render(request, "dashboard_bokeh.html", {
        "bokeh_graphs": bokeh_graphs,
        "graphs_html": graphs_html,
        "categories_data": Category.objects.values_list("name", "description"),
    })


def generate_dataframe_response(queryset):
    return JsonResponse(queryset, safe=False)


def donations_by_category_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_donations_by_category(projects)

    return generate_dataframe_response(data)


def average_donation_by_category_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_average_donation_by_category(projects)

    return generate_dataframe_response(data)


def donations_per_project_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_donations_per_project(projects)

    return generate_dataframe_response(data)


def followers_per_project_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_followers_per_project(projects)

    return generate_dataframe_response(data)


def highest_goal_projects_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_highest_goal_projects(projects)

    return generate_dataframe_response(data)


def project_status_distribution_view(request):
    projects = project_repository.get_all_projects()

    data = project_repository.get_project_status_distribution(projects)

    return generate_dataframe_response(data)


def analyze_model_attributes(request):
    if request.method == "POST":
        form = ModelAttributeForm(request.POST)

        model_name = request.POST.get("model")
        form.set_attributes_choices(model_name)

        if form.is_valid():
            model_name = form.cleaned_data["model"]
            attributes = form.cleaned_data["attributes"]

            try:
                stats = project_repository.analyze_model_attributes(model_name, attributes)
                return JsonResponse({"statistics": stats}, safe=False)
            except ValueError as e:
                return JsonResponse({"error": str(e)}, status=400)
    else:
        form = ModelAttributeForm()

    return render(request, "analyze_model_attributes.html", {"form": form})


def get_model_attributes(request):
    model_name = request.GET.get("model")
    try:
        attributes = project_repository.get_model_attributes(model_name)
        return JsonResponse({"attributes": attributes})
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)


def performance_dashboard(request):
    test_results = run_crowdfunding_tests()

    context = {
        'test_results': json.dumps(test_results)
    }
    return render(request, 'performance_dashboard.html', context)