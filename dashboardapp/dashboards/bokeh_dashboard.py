import numpy as np
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category10
from bokeh.transform import cumsum
import pandas as pd

def bokeh_donations_by_category(data):
    df = pd.DataFrame(data)
    df.rename(columns={'category__name': 'Category'}, inplace=True)
    source = ColumnDataSource(df)

    p = figure(
        x_range=df['Category'],
        title="Donations by Category",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x='Category',
        top='total_donations',
        width=0.9,
        source=source,
        color="skyblue"
    )
    p.add_tools(HoverTool(tooltips=[("Category", "@Category"), ("Donations", "@total_donations")]))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = 1

    return components(p)


def bokeh_average_donation_by_category(data):
    df = pd.DataFrame(data)
    df.rename(columns={'category__name': 'Category'}, inplace=True)
    source = ColumnDataSource(df)

    p = figure(
        x_range=df['Category'],
        title="Average Donation by Category",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x='Category',
        top='avg_donation',
        width=0.9,
        source=source,
        color="green"
    )
    p.add_tools(HoverTool(tooltips=[("Category", "@Category"), ("Average Donation", "@avg_donation")]))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = 1

    return components(p)


def bokeh_donations_per_project(data):
    df = pd.DataFrame(data)
    df.rename(columns={'title': 'Project'}, inplace=True)
    source = ColumnDataSource(df)

    p = figure(
        x_range=df['Project'],
        title="Donations per Project",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x='Project',
        top='total_donations',
        width=0.9,
        source=source,
        color="orange"
    )
    p.add_tools(HoverTool(tooltips=[("Project", "@Project"), ("Total Donations", "@total_donations")]))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = 1

    return components(p)


def bokeh_followers_per_project(data):
    df = pd.DataFrame(data)
    df.rename(columns={'title': 'Project'}, inplace=True)
    source = ColumnDataSource(df)

    p = figure(
        x_range=df['Project'],
        title="Followers per Project",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x='Project',
        top='total_followers',
        width=0.9,
        source=source,
        color="purple"
    )
    p.add_tools(HoverTool(tooltips=[("Project", "@Project"), ("Followers", "@total_followers")]))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = 1

    return components(p)


def bokeh_highest_goal_projects(data):
    df = pd.DataFrame(data)
    df.rename(columns={'title': 'Project', 'goal_amount': 'Goal'}, inplace=True)
    source = ColumnDataSource(df)

    p = figure(
        x_range=df['Project'],
        title="Projects with Highest Goals",
        toolbar_location=None,
        tools=""
    )
    p.vbar(
        x='Project',
        top='Goal',
        width=0.9,
        source=source,
        color="red"
    )
    p.add_tools(HoverTool(tooltips=[("Project", "@Project"), ("Goal", "@Goal")]))
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xaxis.major_label_orientation = 1

    return components(p)


def bokeh_project_status_distribution(data):
    df = pd.DataFrame(data)
    df.rename(columns={'status': 'Status', 'status_count': 'Count'}, inplace=True)

    df['angle'] = df['Count'] / df['Count'].sum() * 2 * np.pi
    df['color'] = Category10[len(df)] if len(df) <= 10 else Category10[10]

    source = ColumnDataSource(df)

    p = figure(
        title="Project Status Distribution",
        toolbar_location=None,
        tools="hover",
        tooltips=[("Status", "@Status"), ("Count", "@Count")]
    )

    p.wedge(
        x=0.5,
        y=0.5,
        radius=0.6,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white",
        fill_color='color',
        legend_field='Status',
        source=source,
        alpha=0.8
    )
    p.outline_line_color = None
    p.axis.visible = False
    p.grid.visible = False
    p.legend.click_policy = "hide"
    p.legend.location = "center_right"
    p.legend.background_fill_alpha = 0.7

    return components(p)
