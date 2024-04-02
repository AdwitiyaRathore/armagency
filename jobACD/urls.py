from django.urls import path
from . import views

app_name = 'jobACD'

urlpatterns = [
    path('list', views.ACDformList.as_view(), name='acdList'),
    path('<int:pk>', views.ACDformDetails.as_view(), name='acdDetail'),
    path('<int:pk>/update', views.ACDformUpdate.as_view(), name='acdUpdate'),
    path('<int:pk>/acdForm/', views.AcdTemplate.as_view(), name='acdTemplate'),
    
    ## Function based Views...
    path('list/search/', views.search_view, name='search'),
]