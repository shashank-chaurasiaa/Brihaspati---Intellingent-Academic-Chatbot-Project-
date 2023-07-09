from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from Chatbot.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User





# Create your views here.
def index(request):
     return render(request, 'index.html')
     #return HttpResponse("This is Home Page.")

#def os(request):
     return render(request, 'os.html')

def cources(request):
     return render(request, 'cources.html')
     #return HttpResponse("This is Cources Page.")
     

def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          text = request.POST.get('text')
          contact = Contact(name=name, email=email, phone=phone, text=text, date=datetime.today())
          contact.save()
          messages.success(request, 'Message has been sent!')
     return render(request, 'contact.html')
     #return HttpResponse("This is Contact Page.")

def signup(request):
     if request.method =="POST":
          # Get post parameters
          username = request.POST['username']
          email = request.POST['email']
          pass1 = request.POST['pass1']
          pass2 = request.POST['pass2']

          #Check for errorneous inputs

          #Create the user
          myuser = User.objects.create_user(username, email, pass1)
          myuser.save()
          messages.success(request, "Your account has been successfully created.")
          return redirect('Chatbot')
     else:
          return HttpResponse('404 - Not Found')

def handleLogin(request):
     if request.method =="POST":
          # Get post parameters
          loginusername = request.POST['loginusername']
          loginpass = request.POST['loginpass']

          user = authenticate(username = loginusername, password = loginpass)

          if user is not None:
               login(request, user)
               messages.success(request, "Successfully Logged In.")
               return redirect('Chatbot')
          else:
               messages.error(request, "Invalid Credentials Please try again!")
               return redirect('Chatbot')
 
     return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect('Chatbot')




""" @login_required
def submit_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.status = 'pending'
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'submit_question.html', {'form': form})

@login_required
def question_list(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, 'question_list.html', {'questions': questions})


@login_required
def review_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher')
        if teacher_id:
            teacher = User.objects.get(pk=teacher_id)
            question.teacher = teacher
            question.status = 'approved'
        else:
            question.status = 'rejected'

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html' """