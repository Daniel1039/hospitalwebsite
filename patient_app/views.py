# from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage, message
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.contrib.auth.views import LoginView as AuthLoginView
# from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect




# Create your views here. 
# 
class HomeTemplateView(TemplateView):
    template_name= 'index.html'
    def post(self, request):
            name = request.POST.get("form-name")
            email = request.POST.get("form-email")
            phone = request.POST.get("form-phone")
            message = request.POST.get("form-message")

            email = EmailMessage(
                subject= f"{name} from doctor family.",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            email.send()
            messages.success(request, "Email sent successfully! we will get back to you in the next 5 min")
            return render(request, 'contact.html', {})
        
    
class AboutTemplateView(TemplateView):
    template_name ='about.html'
    
    
    
class ContactTemplateView(TemplateView):
    template_name= 'contact.html'
    
class LoginView(AuthLoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('manage')

    def get_success_url(self):
        return self.success_url or self.get_redirect_url() or reverse_lazy('manage')

# views.py


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
  
class AppointmentTemplateView(TemplateView):
    template_name= 'appointment.html'
    def post(self, request):
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        email= request.POST.get('email')
        mobile= request.POST.get('mobile')
        message= request.POST.get('request')
        
        appointment=Appointment.objects.create (
            first_name = fname,
            last_name= lname,
            email =email,
            phone= mobile,
            request= message,
        )
        appointment.save()
        
        messages.add_message(request, messages.SUCCESS, f" thanks {fname} for making an appointment, we will email you Asap")
        return render(request, 'appointment.html', {})

class ManageAppointmentTemplateView(LoginRequiredMixin,ListView):
    template_name='manage-appointments.html'
    login_url = '/login/'
    model=Appointment
    context_object_name= 'appointments'
    paginate_by = 3
    
    
    def post(self, request):
        date = request.POST.get("date")
        
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()
        
        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        
        return render(request, 'manage-appointments.html', {})
  

    
    def get_context_data(self,*args, **kwargs):
         context = super().get_context_data(*args, **kwargs)
         appointments = Appointment.objects.all()   
         context.update({
              
            "title":"Manage Appointments"
        })  
         return context
     
    




