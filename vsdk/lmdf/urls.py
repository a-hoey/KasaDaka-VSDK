"""lmdf URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^lmdf/$', views.index, name='index'),
	url(r'^lmdf/index-fr$', views.indexfr, name='indexfr'),
	url(r'^lmdf/wiki$', views.wiki, name='wiki'),
	url(r'^lmdf/wiki-fr$', views.wikifr, name='wikifr'),
	url(r'^lmdf/symptoms$', views.symptoms, name='symptoms'),
	url(r'^lmdf/symptoms-fr$', views.symptomsfr, name='symptomsfr'),
	url(r'^lmdf/patients$', views.patients, name='patients'),
	url(r'^lmdf/patient/(?P<patient_id>[0-9]+)$', views.patient_detail, name='patient-detail'),
	url(r'^lmdf/patient-fr/(?P<patient_id>[0-9]+)$', views.patient_detail_fr, name='patient-detail-fr'),
	url(r'^lmdf/patients-fr$', views.patientsfr, name='patientsfr'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
