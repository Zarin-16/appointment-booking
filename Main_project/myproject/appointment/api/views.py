from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from appointment.models import Appointment
from .serializers import AppointmentSerializer

@api_view(['GET','POST'])
def appointment_list(request):
    if request.method == 'GET':
        appointment_list=Appointment.objects.all()
        serializer=AppointmentSerializer( appointment_list, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
        return Response(serializer.data)

@api_view(['DELETE','PUT'])
def remove_appointment(request,pk):
    if request.method == 'DELETE':  
        appointment_list=Appointment.objects.get(pk=pk)
        appointment_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    if request.method == 'PUT':
        appointment_list=Appointment.objects.get(pk=pk)
        serializer = AppointmentSerializer(appointment_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['PUT'])
# def appointment_update(request,pk):
#     if request.method == 'PUT':
#         appointment_list=Appointment.objects.get(pk=pk)
#         serializer = AppointmentSerializer(appointment_list, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
      
#         return Response(status=status.HTTP_204_NO_CONTENT)