from django.db import models, IntegrityError
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core.mail import send_mail




class EmployeeAccountManager(BaseUserManager):
    def create_employee(self , matricule , password, **extra_fields ):
        if not matricule or len(matricule) <= 0 : 
            raise  ValueError("matricule field is required !")
        if not password :
            raise ValueError("Password is must !")
        employee = self.model(matricule=matricule,username=matricule, **extra_fields)
        employee.set_password(password)
        
        try:
                employee.save(using=self._db)
        except IntegrityError:
            raise IntegrityError('An employee already uses this matricule')
        return employee
    def create_superuser(self, matricule, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_employee(matricule, password, **extra_fields)
    
class EmployeeAccount(AbstractUser):
    matricule = models.CharField(max_length=20 , unique = True)   
    points = models.BigIntegerField(default=0)
    
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length = 200 )
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    
    USERNAME_FIELD = "matricule"
      
    # defining the manager for the UserAccount model
    objects = EmployeeAccountManager()
      
    def __str__(self):
        return str(self.matricule)
      
    def has_perm(self , perm, obj = None):
        return self.is_admin
      
    def has_module_perms(self , app_label):
        return True
          