from django.urls import path
from . import views
from .views import VaccinationRegistrationView

urlpatterns = [
    path('', views.AppointmentView.as_view(), name="appointment"),
    path('register-vaccination/', VaccinationRegistrationView.as_view(), name='vaccination_registration')
]

