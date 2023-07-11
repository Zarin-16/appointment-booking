from django.db import models


class Appointment(models.Model):
    patient_name = models.CharField(max_length=255, blank= True)
    phone_number = models.CharField(max_length=11, blank= True)
    doctor_name = models.CharField(max_length=255, blank= True)
    department = models.CharField(max_length=100, blank= True)
    appointment_date = models.DateTimeField(null = True)
    
    
    
    
    
