"""Techblog URL Configuration

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
from django.urls import path
from django.conf.urls import url,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    url('',include('blog.urls')),
    url('bot/',include('bot.urls')),
    path('accounts/', include('allauth.urls')),
    path('ide/',include('ide.urls')),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('neditor/', include('neditor.urls')),

    #for password reset if some non-solvable error comes
    #url(r'^', include('django.contrib.auth.urls')),   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
