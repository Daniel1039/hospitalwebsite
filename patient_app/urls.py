
from django.urls import path


from .views import  HomeTemplateView, AboutTemplateView, ContactTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView,LoginView,CustomLogoutView

urlpatterns = [
    
    path('',  HomeTemplateView.as_view(), name="home"),
    path('about/',  AboutTemplateView.as_view(), name="about"),
    path('contact/',  ContactTemplateView.as_view(), name="contact"),
    path('make-an-appointment/',  AppointmentTemplateView.as_view(), name="appointment"),
    path('login/', LoginView.as_view(), name='login'),
    path('manage-appointment/',  ManageAppointmentTemplateView.as_view(), name="manage"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
     
]
    
