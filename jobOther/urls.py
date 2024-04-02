from django.urls import path
from . import views

app_name = 'jobOther'

urlpatterns = [
    path('list', views.JobOtherList.as_view(), name='otherList'),
    path('<int:pk>', views.JobOtherDetails.as_view(), name='otherDetail'),
    path('<int:pk>/update', views.JobOtherUpdate.as_view(), name='otherUpdate'),

    ## Function based Views...
    path('list/search/', views.search_view, name='search'),
]