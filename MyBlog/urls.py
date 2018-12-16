"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import re_path, include, url
from django.urls import path


#re_path 和path区别
"""
re_path 用于正则匹配, 并且正则后面的“,”后加空格，避免警告
path 则不用正则
"""


urlpatterns = [
    re_path(r'^polls/', include('polls.urls')),
    url(r'^zone/', admin.site.urls),
    re_path('', include('polls.urls'))
]
