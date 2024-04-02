from django.urls import path
from . import views

app_name = 'jobVGM'

urlpatterns = [
    # path('', views.VGMformView.as_view(), name='vgmForm'),
    path('list', views.VGMformList.as_view(), name='vgmList'),
    path('<int:pk>', views.VGMformDetails.as_view(), name='vgmDetail'),
    path('<int:pk>/update', views.VGMformUpdate.as_view(), name='vgmUpdate'),

    ## Function based Views...
    path('list/search/', views.search_view, name='search'),

    ## VGM Type form urls...
    path('type1/<int:pk>/form1', views.VgmForm1Detail.as_view(), name='type1Detail'),
    path('type2/<int:pk>/form2', views.VgmForm2Detail.as_view(), name='type2Detail'),
    path('type3/<int:pk>/form3', views.VgmForm3Detail.as_view(), name='type3Detail'),
    path('type4/<int:pk>/form4', views.VgmForm4Detail.as_view(), name='type4Detail'),
]