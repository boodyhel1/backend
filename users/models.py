from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
    
        return self.email
    def check_password(self, raw_password):
        """لتأكيد كلمة المرور المشفرة."""
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        """لتشفير كلمة المرور."""
        self.password = make_password(raw_password)
    
    def update_last_login(self):
        """تحديث حقل last_login عند تسجيل الدخول"""
        self.last_login = timezone.now()
        self.save()

class Teacher(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)

    
    last_login = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save()