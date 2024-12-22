from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
import logging

logger = logging.getLogger(__name__)

# Profile view showing quiz progress and user details
@login_required
def profile_view(request):
    user = request.user
    quiz_progress = QuizProgress.objects.filter(user=user)

    total_quizzes = quiz_progress.count()
    total_score = sum([progress.score for progress in quiz_progress])
    average_score = total_score / total_quizzes if total_quizzes > 0 else 0

    context = {
        'user': user,
        'quiz_progress': quiz_progress,
        'total_quizzes': total_quizzes,
        'average_score': average_score,
    }
    return render(request, 'profile/profile.html', context)

# Sign-up view for user registration
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Logout view with logging
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        logger.info('CustomLogoutView called')
        return self.post(request, *args, **kwargs)

# Profile edit view to allow users to update their profile
class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
