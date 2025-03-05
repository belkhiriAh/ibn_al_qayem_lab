from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from results.models import LabResult

# Create your views here.

def home(request):
    if request.method == 'POST':
        result_number = request.POST.get('result_number')
        try:
            result = LabResult.objects.get(result_number=result_number, is_active=True)
            return redirect('verify_result', result_number=result_number)
        except LabResult.DoesNotExist:
            messages.error(request, _('رقم النتيجة غير موجود'))
            return redirect('home')
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        # Here you can add email sending functionality
        messages.success(request, _('تم إرسال رسالتك بنجاح!'))
    return render(request, 'core/contact.html')

def location(request):
    return render(request, 'core/location.html')
