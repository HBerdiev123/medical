"""med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from sitetree.sitetreeapp import register_i18n_trees
from . import views

register_i18n_trees(['menu',])

urlpatterns = i18n_patterns(
    path('', views.index, name='home'),
    path('404', views.error_404),
    path(_('sign-up'), views.sign_up),
    path(_('login'), views.login),
    path(_('contacts/'), views.contacts),
    path(_('search/'), views.post_search, name='search'),
    path(_('blog/'), include('blog.urls', namespace='blog')),
    path(_('pages/'), include('pages.urls', namespace='pages')),
    path(_('doctors/'), include('doctors.urls', namespace='doctor')),
    path(_('appointment/'), include('appointment.urls', namespace='appointment')),
    path(_('admin/'), admin.site.urls),
    path(_('backoffice/'), include('backoffice.urls', namespace='backoffice')),
    path('rosetta/', include('rosetta.urls')),
    path('emails/', include('emails.urls', namespace='emails')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('profile/', include('profiles.urls', namespace="profile")),
)



urlpatterns += (
    path('i18n/', include('django.conf.urls.i18n')),
    )

if settings.DEBUG:
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
