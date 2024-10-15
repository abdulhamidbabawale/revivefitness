from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from model_utils import Choices
# Create your models here.

class CustomUserManagement(UserManager):
    def _create_user(self,email,password, **extra_fields):
        if not email:
            raise ValueError("you have not provided a valid email address")
        email= self.normalize_email(email)
        user= self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_user(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)

    def create_superuser(self,email=None,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email= models.EmailField(blank=True, default='', unique=True)
    fname = models.CharField(max_length=255, blank=True)
    lname = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True)
    profile_picture = models.ImageField(upload_to='user_avatars/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True,null=True)
    updated_at= models.DateTimeField(auto_now=True)
    email_verification_code= models.CharField(max_length=5, blank=True, null=True)
    email_verification_expiry = models.DateTimeField(blank=True, null=True)

    # STATUS = Choices('draft', 'published')
class Plans(models.Model):
    plan_name=models.CharField(max_length=25, unique=True,blank=False)
    plan_price=models.IntegerField(blank=False)

class Benefits(models.Model):
    planid=models.ForeignKey(Plans, on_delete=models.CASCADE ,related_name='plans_benefit')
    perk=models.CharField(max_length=95,unique=True,null=True,blank=True)
    is_instandard=models.BooleanField(default=False)
    is_inplatinum=models.BooleanField(default=False)

class Classes(models.Model):
    classs_img = models.ImageField(upload_to='images/')
    class_name = models.CharField(max_length=100,unique=True)
    decription=models.TextField(null=False,blank=False)


