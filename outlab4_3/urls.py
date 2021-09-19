"""outlab4_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #path('home/',views.home,name='home2'),
    #path('logout/',view.logout,name='logout'),
    path('register/',views.register,name = 'register'),
    path('index/',views.index,name='index'),
    path('update/',views.update_profile,name='update'),
    path('explore/',views.explore,name='explore'),
    path('explore/display/',views.display,name='display'),
    path('updatenow/',views.update_now,name='update_now')
]
