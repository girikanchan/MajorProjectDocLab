from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser



class Manager(BaseUserManager):
    def create_user(self,email,name,date_of_birth,gender,occupation,contno,id_type,id_issue,id_number,issue_state,issue_date,add_type,address,nation,state,district,pincode,password=None,password2 = None):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            email = self.normalize_email(email),name = name, date_of_birth= date_of_birth,gender = gender,occupation=occupation,contno= contno,id_issue=id_issue,id_type= id_type,id_number=id_number,
            issue_state= issue_state,issue_date= issue_date,add_type= add_type,address= address,nation=nation,state=state,district=district,pincode=pincode)

        user.set_password(password)
        user.save(using = self.db)
        return user
        
    def create_superuser(self,email,name,password=None):
        user = self.create_user(
            email,password=password,
            name=name
        )

        user.is_admin = True
        user.save(using=self.db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',max_length=255,unique=True)
    date_of_birth = models.DateField()
    name = models.CharField(max_length=200)
    contno = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    id_type = models.CharField(max_length=200)
    id_issue = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    issue_state = models.CharField(max_length=200)
    issue_date = models.DateField()
    add_type = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    nation = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    pincode = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Manager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','date_of_birth','gender','occupation','contno','id_type','id_issue','id_number','issue_state','issue_date','add_type','address','nation','state','district','pincode']

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj = None):
        "Does the user have a specific permission?"
        return self.is_admin
    
    def has_module_perm(self,app_label):
        "Does the user have permissions to view the app 'app level'?"
        return True
    
    @property
    def is_staff(self):
        "Is the user is a member of staff?"
        return self.is_active

