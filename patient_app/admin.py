from django.contrib import admin
from .models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sent_date' )
    search_fields = ['first_name', 'last_name', 'email']   
# Register your models here.
admin.site.register(Appointment, AppointmentAdmin)  


