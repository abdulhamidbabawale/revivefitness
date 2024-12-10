from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser,PermissionsMixin
from model_utils import Choices
from cloudinary.models import CloudinaryField
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
    date_of_birth = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined= models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True,null=True)
    updated_at= models.DateTimeField(auto_now=True)
    email_verification_code= models.CharField(max_length=5, blank=True, null=True)
    email_verification_expiry = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManagement()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD='email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # STATUS = Choices('draft', 'published')
class Plans(models.Model):
    STANDARD ='standard'
    PLATINUM='platinum'
    PLAN_CHOICES=[
     ( STANDARD ,'Standard'),
     ( PLATINUM,'Platinum')
    ]
    plan_name=models.CharField(max_length=15,choices=PLAN_CHOICES)
    plan_price=models.IntegerField(blank=False)

class Classes(models.Model):
    # classs_img = models.ImageField(upload_to='images/')
    classs_img = CloudinaryField('image',folder='revive fitness/classes')
    class_name = models.CharField(max_length=100,unique=True)
    decription=models.TextField(null=False,blank=False)

class PlanDuration(models.Model):
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    YEARLY = 'yearly'
    DURATION_CHOICES = [
        (MONTHLY, 'Monthly'),
        (QUARTERLY, 'Quarterly'),
        (YEARLY, 'Yearly')
    ]
    userid=models.ForeignKey(User,on_delete=models.CASCADE ,related_name='plans_duration_userid')
    planid=models.ForeignKey(Plans, on_delete=models.CASCADE ,related_name='plans_duration_planid')
    plan_duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE, related_name='classes_plan_duration')
    # plan_duration=Choices('monthly', 'quaterly', 'yearly')
    total_price=models.IntegerField(null=True,blank=True)
    is_active_plan=models.BooleanField(default=True)
    is_expired=models.BooleanField(default=False)
    date_registered=models.DateTimeField(auto_now_add=True)
    expiry_date=models.DateTimeField(auto_now=True)

class Benefits(models.Model):
    planid=models.ForeignKey(Plans, on_delete=models.CASCADE ,related_name='plans_benefit')
    perk=models.CharField(max_length=95,unique=True,null=True,blank=True)
    is_instandard=models.BooleanField(default=False)
    is_inplatinum=models.BooleanField(default=False)



class UserProfile(models.Model):
    userid=models.OneToOneField(User,on_delete=models.CASCADE ,related_name='profile_userid')
    profile_picture = CloudinaryField('image',folder='revive fitness/profile_pic')
    gender=models.CharField(max_length=25,null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    plan_data = models.ForeignKey(PlanDuration, on_delete=models.SET_NULL, null=True, blank=True, related_name='profiles_plan_data')

