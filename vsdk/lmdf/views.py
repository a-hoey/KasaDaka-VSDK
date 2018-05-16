from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _

from .models import *

def index(request):
	return render(request, 'lmdf/index.html', {})

def indexfr(request):
	return render(request, 'lmdf/index-fr.html', {})

def wiki(request):
	return render(request, 'lmdf/wiki.html', {})

def wikifr(request):
	return render(request, 'lmdf/wiki-fr.html', {})

def symptoms(request):
	symptoms = Symptoms.objects.all
	cases1 = Patient.objects.filter(symptoms__id=1)
	cases2 = Patient.objects.filter(symptoms__id=2)
	cases3 = Patient.objects.filter(symptoms__id=3)
	cases4 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=1)
	cases5 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=2)
	cases6 = Patient.objects.filter(symptoms__id=1).filter(symptoms__id=2)
	cases7 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=1).filter(symptoms__id=2)
	return render(request, 'lmdf/symptoms.html', {'symptoms': symptoms,
												 'cases1': cases1,
												 'cases2': cases2,
												 'cases3': cases3,
												 'cases4': cases4,
												 'cases5': cases5,
												 'cases6': cases6,
												 'cases7': cases7,
												 })

def symptomsfr(request):
	symptoms = Symptoms.objects.values('symptom_fr')
	cases1 = Patient.objects.filter(symptoms__id=1)
	cases2 = Patient.objects.filter(symptoms__id=2)
	cases3 = Patient.objects.filter(symptoms__id=3)
	cases4 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=1)
	cases5 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=2)
	cases6 = Patient.objects.filter(symptoms__id=1).filter(symptoms__id=2)
	cases7 = Patient.objects.filter(symptoms__id=3).filter(symptoms__id=1).filter(symptoms__id=2)
	return render(request, 'lmdf/symptoms-fr.html', {'symptoms': symptoms,
													'cases1': cases1,
												 	'cases2': cases2,
												 	'cases3': cases3,
												 	'cases4': cases4,
												 	'cases5': cases5,
												 	'cases6': cases6,
												 	'cases7': cases7,
													})

def patients(request):
	patients = Patient.objects.all()
	return render(request, 'lmdf/patients.html', {'patients': patients})

def patientsfr(request):
	patients = Patient.objects.all()
	return render(request, 'lmdf/patients-fr.html', {'patients': patients})

def patient_detail(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'lmdf/patient_detail.html', {'patient': patient})

def patient_detail_fr(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'lmdf/patient_detail-fr.html', {'patient': patient})