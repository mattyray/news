from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Custom form for user creation
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Reference your custom user model
        fields = ('username', 'email', 'age', 'bio', 'profile_picture')

# Custom form for user change/edit
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'bio', 'profile_picture')
