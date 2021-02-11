from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
from django.utils.translation import ugettext_lazy as _
from django_resized import ResizedImageField

# # Create your models here.
# class AccountManager(BaseUserManager):
#     def create_user(self, email ,password, **extra_fields):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not password:
#             raise ValueError("Users must enter password")
#         user = self.model(
#             email = self.normalize_email(email),
#             **extra_fields
#             )
#         user.set_password(password)
#         user.is_active = True
#         user.save(using=self._db)
#         return user
    
#     def create_staffuser(self, email, password):
#         user = self.create_user(email,password=password)
#         user.is_staff = True
#         user.is_active = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             password=password,
#             username=username
#             )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.is_active = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
    
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.EmailField(max_length=30, unique=False, default='')
#     date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last_login', auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     company_name = models.CharField(max_length=1000)
#     alias_name = models.CharField(max_length=255)
#     phone = models.IntegerField(default=0)
    
#     objects = AccountManager()
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     """Create a Token instance for any User instance created."""
#     if created:
#         Token.objects.get_or_create(user=instance)


class Product_category(models.Model):
	product_type = models.CharField(max_length=500)
	product_name = models.CharField(max_length=500)
	approved_by_admin = models.BooleanField(default=False)

# add user in product table and review system for seller specific product
class Product(models.Model):
	product_category = models.ForeignKey(Product_category, models.CASCADE, related_name='product')
	cost = models.IntegerField(default=0)
	product_img = ResizedImageField(size=[100, 100], upload_to='images/',null = True, blank=False)



