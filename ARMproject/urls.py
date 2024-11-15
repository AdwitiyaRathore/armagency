"""
URL configuration for ARMproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='home'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('entry/', views.Entry.as_view(), name='entry'), # after login where to go url.
    path('exit/', views.Exit.as_view(), name='exit'), # after logout where to go url.

    ## jobData App...
    path('jobData/', include('jobData.urls'), name='jobData'),

    ## jobVGM App...
    path('jobVGM/', include('jobVGM.urls'), name='jobVGM'),

    ## jobBOL App...
    path('jobBOL/', include('jobBOL.urls'), name='jobBOL'),

    ## jobACD App...
    path('jobACD/', include('jobACD.urls'), name='jobACD'),

    ## stuffingSheet App...
    path('stuffingSheet/', include('stuffingSheet.urls'), name='stuffingSheet'),

    ## jobOther App...
    path('jobOther/', include('jobOther.urls'), name='jobOther'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)