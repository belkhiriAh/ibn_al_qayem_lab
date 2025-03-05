from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import LabResult
from django.contrib.auth.decorators import login_required

# Create your views here.

def verify_result(request, result_number):
    result = get_object_or_404(LabResult, result_number=result_number, is_active=True)
    
    if request.method == 'POST':
        password = request.POST.get('password')
        if password == result.password:
            # Password correct, show result
            return render(request, 'results/view_result.html', {'result': result, 'verified': True})
        else:
            messages.error(request, _('كلمة المرور غير صحيحة'))
    
    # Show password entry form
    return render(request, 'results/verify_result.html', {'result_number': result_number})

@login_required
def manage_results(request):
    results = LabResult.objects.all().order_by('-date_created')
    return render(request, 'results/manage_results.html', {'results': results})

@login_required
def add_result(request):
    if request.method == 'POST':
        result_image = request.FILES.get('result_image')
        is_active = request.POST.get('is_active') == 'on'
        
        if result_image:
            result = LabResult.objects.create(
                result_image=result_image,
                is_active=is_active
            )
            messages.success(request, _('تم إضافة النتيجة بنجاح'))
            return redirect('manage_results')
        else:
            messages.error(request, _('الرجاء اختيار صورة النتيجة'))
    
    return render(request, 'results/add_result.html')

@login_required
def edit_result(request, result_number):
    result = get_object_or_404(LabResult, result_number=result_number)
    
    if request.method == 'POST':
        result_image = request.FILES.get('result_image')
        is_active = request.POST.get('is_active') == 'on'
        
        if result_image:
            result.result_image = result_image
        result.is_active = is_active
        result.save()
        
        messages.success(request, _('تم تحديث النتيجة بنجاح'))
        return redirect('manage_results')
    
    return render(request, 'results/edit_result.html', {'result': result})

@login_required
def delete_result(request, result_number):
    result = get_object_or_404(LabResult, result_number=result_number)
    
    if request.method == 'POST':
        result.delete()
        messages.success(request, _('تم حذف النتيجة بنجاح'))
        return redirect('manage_results')
    
    return render(request, 'results/delete_result.html', {'result': result})
