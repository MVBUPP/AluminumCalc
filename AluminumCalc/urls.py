"""
URL configuration for AluminumCalc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from AluminumCalcApp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    #OUR HOME PAGE
    path('', views.home, name='home'),
    #CREATE PAGE
    path('create/', views.create, name='create'),
    #UPDATE PAGE
    path('update/', views.update, name='update'),

    path('create/insert/', views.insert12_2UserTolerance, name="insert12_2UserTolerance")
]
