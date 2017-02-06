"""css URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    # BASE_URL/Home* addresses
    url('^$', views.IndexView, name='index'),
    url(r'^home/', include([
        url('^$', views.HomeView, name='home'),
        url('^schedulers/$', views.SchedulersView, name='schedulers'),
        url('^faculty/$', views.FacultyView, name='faculty'),
        url('^rooms/$', views.RoomsView, name='rooms'),
        url('^courses/$', views.CoursesView, name='courses'),
    ])),
    url(r'^faq/', views.FAQView, name='faq'),
    url(r'^admin/', admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

