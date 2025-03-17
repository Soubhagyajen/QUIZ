from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option, UserQuiz,QuizAttempt
from .forms import QuizForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Add a new quiz
@login_required
@login_required
def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'add_quiz.html', {'form': form})


# List all quizzes
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

# Attempt a quiz

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Option, UserQuiz
from django.contrib.auth.decorators import login_required

def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        score = 0
        correct_answers = 0
        wrong_answers = 0
        total_questions = questions.count()

        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            print(f"Selected Option ID for Question {question.id}: {selected_option_id}")
            
            if selected_option_id:
                try:
                    selected_option = Option.objects.get(id=selected_option_id)
                    print(f"Selected Option: {selected_option.text}, Is Correct: {selected_option.is_correct}")
                    if selected_option.is_correct:
                        score += 1
                        correct_answers += 1
                    else:
                        wrong_answers += 1
                except Option.DoesNotExist:
                    print(f"No Option found with ID {selected_option_id}")
                    wrong_answers += 1
            else:
                print(f"No option selected for Question {question.id}")
                wrong_answers += 1
        
        # Pass results to the template
        return render(request, 'attempt_quiz.html', {
            'quiz': quiz,
            'score': score,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'wrong_answers': wrong_answers
        })

    return render(request, 'attempt_quiz.html', {'quiz': quiz, 'questions': questions, 'score': None})

# View quiz results
@login_required
def result(request, user_quiz_id):
    user_quiz = get_object_or_404(UserQuiz, id=user_quiz_id, user=request.user)
    return render(request, 'result.html', {'user_quiz': user_quiz})

# User signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('quiz_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    user_attempts = QuizAttempt.objects.filter(user=request.user).order_by('-timestamp')
    context = {
        'user_attempts': user_attempts,
    }
    return render(request, 'dashboard.html', context)