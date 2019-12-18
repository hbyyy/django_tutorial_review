from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from polls.models import Question


def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f'detail {question_id}')


def results(request, question_id):
    return HttpResponse(f'results {question_id}')


def vote(request, question_id):
    return HttpResponse(f'vote {question_id}')
