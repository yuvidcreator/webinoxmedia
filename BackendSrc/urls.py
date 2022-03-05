"""BackendSrc URL Configuration

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

import os
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path(os.environ.get('SECRET_ADMIN_URL') + '/admin/', admin.site.urls),
    path('admin/', admin.site.urls),

    path('', HomePage, name="Home Page"),
    # path('services/', ServicesPage, name="Services Page"),
    path('contact/', ContactPage, name="Contact Page"),
    path('thanks/', ThanksPage, name="Thanks Page"),
    # path('about/', AboutPage, name="About Page"),
    # path('faq/', FaqPage, name="FAQ Page"),
    # path('case-studies/', CaseStudiesPage, name="Case Studies Page"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
