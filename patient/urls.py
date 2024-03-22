from django.urls import path
from . import views
from django.conf.urls.static import static
urlpatterns= [    
    path('',views.home,name='home'),
    path('doctor/', views.doctor_login, name='doctor_login'),
    path('doctor/login',views.doctor_login,name='doctor_login'),
    path('doctor/logout',views.doctor_logout,name='doctor_logout'),
    path('doctor/reset-password',views.doctor_reset_password,name='doctor_reset_password'),
    path('doctor/dashboard',views.doctor_dashboard,name='doctor_dashboard'),
    path('doctor/quick-add-patient',views.quick_add_patient,name='quick_add_patient'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
