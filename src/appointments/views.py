from django.shortcuts import render, get_object_or_404
from .models import AppointmentsList


# Create your views here.

# Retreive all till 10 (pagination) recent appointments
def aptmt_list_view(request):
    qs = AppointmentsList.objects.all()
    template_name = 'appointments.html'
    context = {"object_list": qs, "title": "Upcoming Appointments"}
    return render(request, template_name, context)


# Create requests for new appointment, will go to reception
# and they will confirm
def aptmt_create_view(request):
    template_name = 'appointments/new.html'
    context = {"form": None, "title": "Request Appointment"}
    return render(request, template_name, context)


# see details of a previously requested appointment
def aptmt_details_view(request, id):
    obj = get_object_or_404(AppointmentsList, id=id)
    template_name = 'appointments/details.html'
    context = {"object": obj, "title": "Appointment Details"}
    return render(request, template_name, context)


# update details of a previously requested appointment
def aptmt_update_view(request, id):
    obj = get_object_or_404(AppointmentsList, id=id)
    template_name = 'appointments/update.html'
    context = {"object": obj, "title": "Update Appointment"}
    return render(request, template_name, context)


# delete a previously requested appointment
def aptmt_delete_view(request, id):
    obj = get_object_or_404(AppointmentsList, id=id)
    template_name = 'appointments/delete.html'
    context = {"object": obj, "title": "Delete Appointment"}
    return render(request, template_name, context)