from django.urls import path
from .views import SignUpView, CustomLogoutView, profile_view, ProfileEditView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),  # Use profile_view here
    path('profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
]
