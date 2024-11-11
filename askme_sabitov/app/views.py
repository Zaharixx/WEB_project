from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .utils import paginate
import copy

QUESTIONS = []
for i in range(1,31):
  QUESTIONS.append({
    'title': f'title {i}',
    'id': i,
    'text': f'This is text for question {i}'
  })

ANSWERS = []
for i in range(1,21):
   ANSWERS.append({
      'id': i,
      'text': f'This is text for answer {i}',
      'correct': True
   })

def index(request):
    page = paginate(QUESTIONS, request, 5)
    return render(request, 'index.html', context={'questions': page.object_list,'page_obj': page})

def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page = paginate(hot_questions, request, 5)
    return render(request, 'hot.html', context={'questions': page.object_list, 'page_obj': page})

def question(request, question_id):
   question = QUESTIONS[question_id - 1]
   page = paginate(ANSWERS, request, 4)
   return render(request, 'question.html', context={'item': question,
                                                    'answers': page.object_list,
                                                    'page_obj': page})

def base(request):
   return render(request, 'layouts/base.html')

def settings(request):
   return render(request, 'user_settings.html')

def ask(request):
   return render(request, 'ask.html')

def login(request):
   return render(request, 'login.html')

def signup(request):
   return render(request, 'signup.html')

def tag(request, tag_name):
   tagged_questions = QUESTIONS[7:14]
   page = paginate(tagged_questions, request, 5)
   return render(request, 'tag.html', context={'tagged_questions': page.object_list,
                                                'tag_name' : tag_name,
                                                'page_obj' : page, 
                                                })  