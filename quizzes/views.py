from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, QuizProgress

# View for taking a quiz
@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        user_answers = request.POST.getlist('answers')
        score = 0

        for question, user_answer in zip(questions, user_answers):
            correct_answer = question.answer_set.get(is_correct=True)
            if str(correct_answer.id) == user_answer:
                score += 1

        # Save user quiz progress
        QuizProgress.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=questions.count()
        )
        return redirect('quiz_results', quiz_id=quiz.id, score=score)

    return render(request, 'quizzes/take_quiz.html', {'quiz': quiz, 'questions': questions})

# View for displaying the quiz results
@login_required
def quiz_results(request, quiz_id, score):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quizzes/quiz_results.html', {
        'quiz': quiz,
        'score': score,
    })
