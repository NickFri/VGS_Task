"""field URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    # ex: /app/5/
    path('<int:data_id>/', views.detail, name='detail'),
    path('vgs/return/<int:data_id>/', views.get_data, name='api.data'),
    path('echo/server/<int:data_id>/', views.check, name='api.checker'),

]
