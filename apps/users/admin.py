from django.contrib import admin
from .models import User
from .forms import UserChangeForm
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm

admin.site.register(User, UserAdmin)