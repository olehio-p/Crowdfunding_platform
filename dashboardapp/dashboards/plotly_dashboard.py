import pandas as pd
import plotly.express as px

def plotly_donations_by_category(data):
   df = pd.DataFrame(data)
   fig = px.bar(
       df,
       x='category__name',
       y='total_donations',
       title='Donations by Category',
       labels={'category__name': 'Category', 'total_donations': 'Total Donations'},
       color='total_donations',
       color_continuous_scale='Viridis'
   )
   fig.update_layout(
       template='plotly_white'
   )
   return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plotly_average_donation_by_category(data):
   df = pd.DataFrame(data)
   fig = px.bar(
       df,
       x='category__name',
       y='avg_donation',
       title='Average Donation by Category',
       labels={'category__name': 'Category', 'avg_donation': 'Average Donation'},
       color='avg_donation',
       color_continuous_scale='Plasma'
   )
   fig.update_layout(
       template='plotly_white'
   )
   return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plotly_donations_per_project(data):
   df = pd.DataFrame(data).sort_values('total_donations', ascending=False).head(10)
   fig = px.bar(
       df,
       x='title',
       y='total_donations',
       title='Top 10 Projects by Total Donations',
       labels={'title': 'Project Title', 'total_donations': 'Total Donations'},
       color='total_donations',
       color_continuous_scale='Blugrn'
   )
   fig.update_layout(
       xaxis_tickangle=-45,
       template='plotly_white'
   )
   return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plotly_followers_per_project(data):
   df = pd.DataFrame(data).sort_values('total_followers', ascending=False).head(10)
   fig = px.bar(
       df,
       x='title',
       y='total_followers',
       title='Top 10 Projects by Followers',
       labels={'title': 'Project Title', 'total_followers': 'Total Followers'},
       color='total_followers',
       color_continuous_scale='Sunset'
   )
   fig.update_layout(
       xaxis_tickangle=-45,
       template='plotly_white'
   )
   return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plotly_highest_goal_projects(data):
   df = pd.DataFrame(data).sort_values('goal_amount', ascending=False).head(10)
   fig = px.bar(
       df,
       x='title',
       y='goal_amount',
       title='Top 10 Projects with Highest Goals',
       labels={'title': 'Project Title', 'goal_amount': 'Goal Amount'},
       color='goal_amount',
       color_continuous_scale='Inferno'
   )
   fig.update_layout(
       xaxis_tickangle=-45,
       template='plotly_white'
   )
   return fig.to_html(full_html=False, include_plotlyjs='cdn')

def plotly_project_status_distribution(data):
   df = pd.DataFrame(data)
   fig = px.pie(
       df,
       names='status',
       values='status_count',
       title='Project Status Distribution',
       labels={'status': 'Project Status', 'status_count': 'Count'},
       color_discrete_sequence=px.colors.qualitative.Pastel
   )
   fig.update_layout(
       template='plotly_white'
   )
   fig.update_traces(textposition='inside', textinfo='percent+label')
   return fig.to_html(full_html=False, include_plotlyjs='cdn')