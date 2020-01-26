from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email,  password=None, phone_no=None, active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.phone_no = phone_no
        user_obj.active = active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None, phone_no=None):
        user = self.create_user(
            email,
            password=password,
            phone_no=phone_no,
            is_staff=True
        )

        return user

    def create_superuser(self, email, password=None, phone_no=None):
        user = self.create_user(
            email,
            password=password,
            phone_no=phone_no,
            is_staff=True,
            is_admin=True
        )

        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_no = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    # this is the main username
    USERNAME_FIELD = 'email'

    # required fields - USERNAME_FIELD (it is email in this case) and password are required by default ... it is used in the cases like python manage.py createsuperuser
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, default=62)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, default='Male', blank=True, null=True)

    def __str__(self):
        return (str(self.user) if self.user else "null")
