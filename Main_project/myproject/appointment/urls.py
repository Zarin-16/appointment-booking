from django.urls import path
from . import views
urlpatterns = [
    path("appointment/",views.appointment, name="home"),
    # path('list/',views.appointment_list,name='appointment_list'),
    # path("appointment/", views.appointment , name="appointment")
  
 ]