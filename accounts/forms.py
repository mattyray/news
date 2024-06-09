from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=(
            'username',
            'email',
            'age',
        )
        #using the meta class to override the default fieldsmby setting the model to customuser defined in models
        #

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models=CustomUser
        fields=(
            'username',
            'email',
            'age',
        )