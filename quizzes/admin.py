from django.contrib import admin
from .models import Quiz, QuizProgress, Question, Answer

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit']
    search_fields = ['title', 'unit__title']

class QuizProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'total_questions', 'date_taken']
    search_fields = ['user__username', 'quiz__title']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizProgress, QuizProgressAdmin)
admin.site.register(Question)
admin.site.register(Answer)
