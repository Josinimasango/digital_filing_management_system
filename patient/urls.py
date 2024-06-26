from django.urls import path
from . import views



urlpatterns= [
    path('',views.home,name='home'),
    path('doctor/login',views.doctor_login,name='doctor_login'),
    path('doctor/logout',views.doctor_logout,name='doctor_logout'),
    path('doctor/reset-password',views.doctor_reset_password,name='doctor_reset_password'),
    path('doctor/dashboard',views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor/quick-add-patient',views.quick_add_patient,name='quick_add_patient'),
    path('doctor/all-patients',views.all_patients,name='all_patients'),
    path('doctor/add',views.add_patient,name='add_patient'),
    path('doctor/update/<int:id>',views.update_patient,name='update_patient'),
    path('doctor/delete/<int:id>',views.delete_patient,name='delete_patient'),
    
    path('patients/email_template',views.email_template,name='email_template'),
]
