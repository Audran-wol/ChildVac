from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views import View
from .models import Slider, Service, Doctor, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView
from hospital.forms import ChildForm, VaccinationForm

# Existing code...

class HomeView(ListView):
    template_name = 'hospital/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Doctor.objects.all()
        return context


class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = "hospital/services.html"


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "hospital/service_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class DoctorListView(ListView):
    template_name = 'hospital/team.html'
    queryset = Doctor.objects.all()
    paginate_by = 8


class DoctorDetailView(DetailView):
    template_name = 'hospital/team-details.html'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctor.objects.all()
        return context


class FaqListView(ListView):
    template_name = 'hospital/faqs.html'
    queryset = Faq.objects.all()


class GalleryListView(ListView):
    template_name = 'hospital/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9


class ContactView(TemplateView):
    template_name = "hospital/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "Heartcare Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+phone,
                message,
                email,
                ['expelmahmud@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, " Email hasbeen sent successfully...")

        return redirect('contact')

class VaccinationRegistrationView(View):
    def get(self, request, *args, **kwargs):
        child_form = ChildForm()
        vaccination_form = VaccinationForm()
        return render(request, "appointment/register_vaccination.html", {'child_form': child_form, 'vaccination_form': vaccination_form})

    def post(self, request, *args, **kwargs):
        child_form = ChildForm(request.POST, request.FILES)
        vaccination_form = VaccinationForm(request.POST)
        if child_form.is_valid() and vaccination_form.is_valid():
            child = child_form.save()
            vaccination = vaccination_form.save(commit=False)
            vaccination.child = child
            vaccination.save()
            messages.success(request, 'Child registered for vaccination successfully')
            return redirect('vaccination_registration')
        return render(request, "appointment/register_vaccination.html", {'child_form': child_form, 'vaccination_form': vaccination_form})
