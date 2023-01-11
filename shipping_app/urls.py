"""shipping_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic.base import TemplateView

from core import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('index.php', TemplateView.as_view(template_name='index.html')),
    path('about.php', TemplateView.as_view(template_name='about.html')),
    path('air-freight.php', TemplateView.as_view(template_name='air-freight.html')),
    path('contact-us.php', TemplateView.as_view(template_name='contact-us.html')),
    path('custom-clearance.php', TemplateView.as_view(template_name='custom-clearance.html')),
    path('land-freight.php', TemplateView.as_view(template_name='land-freight.html')),
    path('removals-relocation.php', TemplateView.as_view(template_name='removals-relocation.html')),
    path('sea-freight.php', TemplateView.as_view(template_name='sea-freight.html')),
    path('service.php', TemplateView.as_view(template_name='service.html')),
    path('services.php', TemplateView.as_view(template_name='service.html')),
    path('warehouse.php', TemplateView.as_view(template_name='warehouse.html')),

    path('tracking.php', views.Tracking.as_view()),
    path('tracking1.php', views.Tracking1.as_view()),
    path('<path:path>', views.serve_static),
]




