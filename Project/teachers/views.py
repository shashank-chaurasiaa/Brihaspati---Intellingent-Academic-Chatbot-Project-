from django.shortcuts import redirect, render, get_object_or_404
from .models import Question
from django.forms import QuestionForm
# Create your views here.

def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions:index')
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'teachers/edit_question.html', context)
