from django.urls import path

from . import views

app_name = 'jobBOL'

urlpatterns = [
    path('list', views.BOLformList.as_view(), name='bolList'),
    path('<int:pk>', views.BOLformDetails.as_view(), name='bolDetail'),
    path('<int:pk>/update', views.BOLformUpdate.as_view(), name='bolUpdate'),

    ## Function based Views...
    path('list/search/', views.search_view, name='search'),
    path('bolTemplate/', views.bol_template, name='bolTemplate'),
]