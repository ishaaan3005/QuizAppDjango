import random
from django.shortcuts import render, redirect
from .models import Question

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'quiz/register.html', {'form': form})

# Initialize the session to store user performance
def get_user_performance(request):
    if 'total_attempted' not in request.session:
        request.session['total_attempted'] = 0
        request.session['correct_answers'] = 0
    return request.session['total_attempted'], request.session['correct_answers']

# Dashboard view
def dashboard(request):
    total_attempted, correct_answers = get_user_performance(request)
    score = (correct_answers / total_attempted * 100) if total_attempted > 0 else 0
    return render(request, 'quiz/dashboard.html', {
        'total_attempted': total_attempted,
        'correct_answers': correct_answers,
        'score': score,
    })

# Quiz view
def quiz(request):
    total_attempted, correct_answers = get_user_performance(request)
    all_questions = list(Question.objects.all())
    
    if 'question_index' not in request.session:
        request.session['question_index'] = 0  # Start at the first question

    current_index = request.session['question_index']
    question = all_questions[current_index]

    if request.method == 'POST':
        user_answer = request.POST.get('answer')  
        correct_answer = request.session.get('correct_answer')

        # Provide feedback based on the user's answer
        if user_answer:
            if user_answer == correct_answer:
                feedback = "Correct!"
                request.session['correct_answers'] += 1
            else:
                feedback = f"Incorrect. The correct answer was: {correct_answer}"
            
            request.session['total_attempted'] += 1
        else:
            feedback = "Please select an answer."

        request.session['correct_answer'] = question.correct_answer

        # Handle the "Next" and "Previous" buttons
        if 'next_question' in request.POST:
            if current_index < len(all_questions) - 1:
                request.session['question_index'] = current_index + 1  # Move to next question
            else:
                request.session['question_index'] = 0  # Loop back to first question

        elif 'previous_question' in request.POST:
            if current_index > 0:
                request.session['question_index'] = current_index - 1  # Go to previous question
            else:
                request.session['question_index'] = len(all_questions) - 1  # Loop to last question

        # Handle the "End Quiz" button
        if 'end_quiz' in request.POST:
            return redirect('dashboard')

        # Redirect to the same page to show the next or previous question
        return render(request, 'quiz/quiz.html', {
            'feedback': feedback,
            'show_feedback': True,
            'question': all_questions[request.session['question_index']], 
        })

    # Store the correct answer in session before rendering the question
    request.session['correct_answer'] = question.correct_answer

    return render(request, 'quiz/quiz.html', {
        'question': question,
        'show_feedback': False,
    })
