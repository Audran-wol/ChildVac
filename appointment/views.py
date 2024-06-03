from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from hospital.models import Doctor
from .models import Appointment
from hospital.forms import ChildForm, VaccinationForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.conf import settings
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'doctors': Doctor.objects.all()
        }
        return render(request, "appointment/index.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')
        if doctor_id:
            doctor = get_object_or_404(Doctor, id=doctor_id)

        if(name and phone and email and doctor and date and time):
            Appointment.objects.create(
                name=name, phone=phone, email=email, doctor=doctor, date=date, time=time, note=note)
            messages.success(request,'Appointment done successfully')
        return redirect('appointment')

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

            # Generate PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Child_Vaccination_Registration.pdf"'
            p = canvas.Canvas(response, pagesize=letter)

            # Add logo
            logo_path = settings.STATIC_ROOT + '/heartcare/images/logo.png'
            p.drawImage(logo_path, 40, 750, width=100, height=50)

            # Add date
            p.setFont("Helvetica", 12)
            p.drawString(450, 750, f"Date: {vaccination.date}")

            # Title
            p.setFont("Helvetica-Bold", 18)
            p.drawCentredString(300, 700, "Child Vaccination Registration")

            # Child details
            data = [
                ['Child\'s Name:', child.name],
                ['Parent\'s Name:', child.parent_name],
                ['Age:', child.age],
                ['Gender:', child.gender],
                ['Vaccine:', vaccination.vaccine.title],
                ['Doctor:', vaccination.doctor.name],
                ['Date:', vaccination.date]
            ]
            table = Table(data, colWidths=[150, 300], rowHeights=30)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 12),
                ('TOPPADDING', (0, 1), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
            ]))
            table.wrapOn(p, 100, 300)
            table.drawOn(p, 100, 450)

            # Signatures
            p.setFont("Helvetica-Bold", 12)
            p.drawString(100, 400, "Parent's Signature:")
            p.rect(250, 390, 200, 30)  # Signature box
            p.drawString(100, 350, "Doctor's Signature:")
            p.rect(250, 340, 200, 30)  # Signature box

            # Message
            p.setFont("Helvetica", 12)
            p.drawString(100, 300, f"Child vaccination will be on {vaccination.date}.")
            p.drawString(100, 280, "Thank you for using our services.")

            # Contact details
            p.drawString(100, 150, "Contact us: +237-653116420 | childvaccination@example.com")
            p.drawString(100, 130, "Cameroon Yaounde st Avenue Kennedy 236")
            p.drawString(100, 130, "In collaboration with ICTUniversity Yaoundé")
            # Border and footer
            p.setStrokeColor(colors.grey)
            p.line(50, 105, 550, 105)
            p.setFont("Helvetica", 9)
            p.drawString(250, 90, "childvaccination.com")

            p.showPage()
            p.save()
            return response

        return render(request, "appointment/register_vaccination.html", {'child_form': child_form, 'vaccination_form': vaccination_form})