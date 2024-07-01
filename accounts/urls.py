from django.urls import path
from .views import signup, patient_dashboard, doctor_dashboard

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
]