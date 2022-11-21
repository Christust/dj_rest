from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords
# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name, last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

    def create_user(self, username, email, name, last_name, password = None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, password = None, **extra_fields):
        return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("Username", unique=True, max_length=100)
    email = models.EmailField("Email", unique=True, max_length=100)
    name = models.CharField("Name", max_length=100, blank=True, null=True)
    last_name = models.CharField("Lastname", max_length=100, blank=True, null=True)
    image = models.ImageField("Image", upload_to="perfil/", max_length=200, height_field=None, width_field=None, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    historical = HistoricalRecords()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "last_name"]

    def natural_key(self):
        return (self.username)

    def __str__(self):
        return f"User {self.username}"
