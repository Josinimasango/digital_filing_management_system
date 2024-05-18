from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages

from.forms import QuickPatientForm,PatientForm
from.models import Patient

def home(request):
    return render(request,'home.html')

# doctor login
def doctor_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user) 
            return redirect('/')    
        else:
            return redirect('doctor_login')    
    return render(request,'login.html',{
        'page_title':'Doctor Login'
    })



# Doctor logout
def doctor_logout(request):
    logout(request) 
    return redirect('doctor_login')

#Reset Password
def doctor_reset_password(request):
    if not request.user.is_authenticated:
       return redirect('doctor_login')
        
        
    if request.method=="POST":
        password=request.POST.get('password')
        request.user.set_password(password)
        messages.success(request, "Password has been successfully changed.")
        return redirect('doctor_login')
    else:    
        return render(request,'reset-password.html')
    
 # doctor dashboard   
def doctor_dashboard(request):
    return render(request,'doctor-dashboard.html')
    
# Doctor Quick Add Patient
def quick_add_patient(request):
    if request.method == 'POST':
        form=QuickPatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully!")
            return redirect('quick_add_patient')    
        else:
            messages.warning(request, "Something went wrong.")
            return redirect('quick_add_patient')  
    else:       
        form=QuickPatientForm
        return render(request,'quick-add-patient-form.html', {
            'form':form
    }) 

# manage patients        
def all_patients(request):
    data=Patient.objects.all().order_by("-id")
    return render(request,'all-patients.html',{'data':data})       

# Doctor Add Patient
def add_patient(request):
    if request.method == 'POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient added successfully!")
            return redirect('add_patient')    
        else:
            messages.warning(request, "Something went wrong.")
            return redirect('add_patient')  
    else:       
        form=PatientForm
        return render(request,'add-patient-form.html', {
            'form':form
    }) 
        
# Doctor Update Patient        
def update_patient(request,id):
    patient=Patient.objects.get(id=id)
    if request.method == 'POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully!")
            return redirect('update_patient',id)    
        else:
            messages.warning(request, "Something went wrong.")
            return redirect('update_patient',id)  
    else:       
        form=PatientForm(instance=patient)
        return render(request,'update-patient-form.html', {
            'form':form
    }) 

def delete_patient(request,id):
    Patient.objects.get(id=id).delete()
    messages.success(request, "Patient deleted successfully!")
    return redirect('all_patients')  

def email_template(request):
    return render(request,'email_template.html')  

def n_patients(request):
    patients=Patient.objects.filter(visit_date__lt=date.today())
    for patient in patients:
        nextVisitDate=patient.visit_date+timedelta(days=patient.next_visit)
        notificationDate=nextVisitDate-timedelta(days=1)
        if notification == date.today:
           print('send notification')
    return render(request, 'n_patients.html',{
    

'patients':patients
})
    