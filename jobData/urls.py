from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'jobData'

urlpatterns = [
    ## Class Based Views....
    path('list', views.jobListView.as_view(), name='jobList'),
    path('<int:pk>', views.JobDetailView.as_view(), name='jobDetail'),
    path('', views.CreateJobView.as_view(), name='createJob'),
    path('<int:pk>/update', views.JobUpdateView.as_view(), name='updateJob'),
    path('<int:pk>/remove', views.JobDeleteView.as_view(), name='deleteJob'),

    ## Function Based Views....
    path('list/search/', views.search_view, name='search'),
    path('Filterlist/', views.jobFilterListView, name='jobFilterList'),
]