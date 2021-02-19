from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, tel, lname, fname, password=None):
        if not email:
            raise ValueError("You need Email!")
        if not tel:
            raise ValueError("You need type Phone number")
        if not lname:
            raise ValueError("You need type Last name!")
        if not fname:
            raise ValueError("You need First name!")

        user = self.model(
            email=self.normalize_email(email),
            tel=tel,
            lname=lname,
            fname=fname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, lname, tel, fname):
        user = self.create_user(
            email=self.normalize_email(email),
            tel = tel,
            lname = lname,
            fname = fname,
            password = password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    fname = models.CharField(verbose_name=_("First Name"), max_length=20)
    lname = models.CharField(verbose_name=_("Last Name"), max_length=20)
    balance = models.DecimalField(verbose_name=_("Balance"), max_digits=30, decimal_places=2, default=0.0)
    tel = models.CharField(verbose_name=_("Phone NUmber"), max_length=15)
    email = models.EmailField(verbose_name=_("Email"), max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name=_("Date Joined"), auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname', 'tel']

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.fname + " " + self.lname

