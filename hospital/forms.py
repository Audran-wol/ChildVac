from django import forms
from .models import Child, Vaccination, Doctor, Service

class ChildForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender")  # Add this line

    class Meta:
        model = Child
        fields = ['name', 'parent_name', 'age', 'gender', 'picture']

class VaccinationForm(forms.ModelForm):
    vaccine = forms.ModelChoiceField(queryset=Service.objects.all(), label="Vaccine")
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), label="Hospital")
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Vaccination
        fields = ['vaccine', 'doctor', 'date']