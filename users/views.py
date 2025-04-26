from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Student 
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')
        birth_date = request.POST.get('birth_date')
        if not all([firstname, lastname, email, password, confirm_password, birth_date]):
            messages.error(request, "All fields are required!")
            return redirect('signup')
          
        if Student.objects.filter(email=email).exists():    
            messages.error(request, "Email already exists.")
            return redirect('signup')
        
        if password < 8 :
            messages.error(request, "password lower than 8")
            return redirect('signup')
    
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        student = Student(firstname = firstname, email = email, lastname = lastname, birth_date = birth_date)
        student.set_password(password)
        student.save()
        
        messages.success(request, "تم إنشاء الحساب بنجاح!")
        return redirect('login')
        

    return render(request, 'signup.html')

def student_login(request):
    if request.method == 'POST':
        email  = request.POST.get('email')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(email=email)

            if student.check_password(password):
                login(request, student)
                return redirect('home2')
            else:
                return render(request, 'login.html', {'error': 'بيانات الدخول غير صحيحة'})
        except Student.DoesNotExist:
            messages.error(request, "البريد الإلكتروني غير موجود!")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
    
