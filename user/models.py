from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class AllUser(BaseUserManager):
    def create_user(self, phone, email, password=None):
        if not email:
            raise ValueError('کاربر باید پست الکترونیکی داشته باشد')
        
        if not phone:
            raise ValueError('کاربر باید شماره تلفن داشته باشد')

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, phone, email, password):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone      = models.CharField(max_length=30, unique=True)
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=255, null=True)
    is_locked  = models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)    
    is_admin   = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email"]
    
    objects = AllUser()

    def __str__(self) -> str:
        return self.phone
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
