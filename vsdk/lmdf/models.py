from django.db import models
from django.utils import timezone
	
	
class Symptoms(models.Model):
	symptom = models.CharField(max_length=30, blank=False)
	symptom_fr = models.CharField(max_length=30, blank=False)
	
	def __str__(self):
		return self.symptom
	
	
class Trimester(models.Model):
	trimester = models.CharField(max_length=20)
	
	def __str__(self):
		return self.trimester
	
class Diagnosis(models.Model):
	diagnosis = models.CharField(max_length=20)
	diagnosis_fr = models.CharField(max_length=20)
	
	def __str__(self):
		return self.diagnosis
	
	
class Patient(models.Model):
	_urls_name = 'lmdf:patient_detail'
	_urls_name = 'lmdf:patient_detail_fr'
	
	casenumber = models.CharField(max_length=20)
	age = models.CharField(max_length=20)
	diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE )
	trimester = models.ForeignKey(Trimester, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	symptoms = models.ManyToManyField(Symptoms)
	comments = models.TextField(max_length=1000)
	commentsfr = models.TextField(max_length=1000)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return "Patient no: " + str(self.id)
	
