from django.db import models
from django.contrib.auth import get_user_model

# Reference to the custom user model
CustomUser = get_user_model()

# The Quiz model
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.ForeignKey('tutorials.Unit', on_delete=models.CASCADE)  # Foreign key to Unit

    def __str__(self):
        return self.title

# Model for tracking user progress on quizzes
class QuizProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - Score: {self.score}/{self.total_questions}"

# Additional models (Question, Answer, etc.)
class Question(models.Model):
    MULTIPLE_CHOICE = 'MC'
    TRUE_FALSE = 'TF'
    QUESTION_TYPES = [
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (TRUE_FALSE, 'True/False'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPES, default=MULTIPLE_CHOICE)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
