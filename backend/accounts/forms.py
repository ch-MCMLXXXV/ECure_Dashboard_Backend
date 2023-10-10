from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff


class StaffCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Staff
        fields = ("email", "first_name", "last_name")


class StaffChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = Staff
        fields = ("email", "first_name", "last_name")
