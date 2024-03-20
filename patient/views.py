from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib import messages

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
    return render(request,'quick-add-patient-form.html') 
