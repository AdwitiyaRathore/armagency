from django.urls import path
from . import views

app_name = 'stuffingSheet'

urlpatterns = [
    path('list', views.StuffingSheetformList.as_view(), name='stuffingSheetList'),
    path('<int:pk>', views.StuffingSheetformDetails.as_view(), name='stuffingSheetDetail'),
    path('<int:pk>/update', views.StuffingSheetformUpdate.as_view(), name='stuffingSheetUpdate'),

    ## Function based Views...
    path('list/search/', views.search_view, name='search'),
    path('stuffingTemplate/', views.stuffingSheetTemplate, name='stuffingSheetTemplate'),
]