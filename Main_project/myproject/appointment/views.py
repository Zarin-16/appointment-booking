from django.shortcuts import render
from .forms import AppointmentForm
from .models import Appointment
from django.http import HttpResponse


def home(request):

    return render(request, "index.html")
def appointment(request):
    if request.method == "POST":
        your_name = request.POST.get('your_name')
        phone_number = request.POST.get('phone_number')
        doctor_name = request.POST.get('doctor_name')
        department = request.POST.get('department')
        appointment_date = request.POST.get('appointment_date')
        appointment = Appointment.objects.create(patient_name= your_name, phone_number = phone_number, doctor_name = doctor_name, department = department, appointment_date = appointment_date)
        # if appointment.save() :
        return render(request,"appointment.html")
    else:
        return render(request, "index.html")
   
 




# def appointment(request):
#     if request.method == "POST":
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, "appointment.html", {"form": form})
#     else:
#         form = AppointmentForm()
#         return render(request, 'index.html', {"form": form})



















    # if request.method == "POST":

    #     your_name = request.POST.get('your_name')
    #     your_number = request.POST.get('your_number')
    #     doctor_name = request.POST.get('doctor_name')
    #     department = request.POST.get('department')
    #     date = request.POST.get('date')

    #     Appointment.objects.create(patient_name= your_name, phone_number = your_number, doctor_name = doctor_name, department = department, appointment_date = date).save()
    #     data = {'your_name':your_name,
    #             'your_number': your_number,
    #             'doctor_name': doctor_name,
    #             'department': department,
    #             'date' : date
    #             }
    #     return render(request, "appointment.html", data)
    # else:
    #     return render(request, "index.html")
       
   
