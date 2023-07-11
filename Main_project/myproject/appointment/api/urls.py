from django.urls import path
from . import views
urlpatterns = [
   
    path('list/',views.appointment_list,name='appointment_list'),
    path('delete/<int:pk>/',views.remove_appointment,name='remove_appointment'),
    path('update/<int:pk>/',views.remove_appointment,name='update_appointment')
    # path("appointment/", views.appointment , name="appointment")
  
 ]