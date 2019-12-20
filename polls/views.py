from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = {'questions': questions}

    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context ={
        'question': question
    }
    return render(request, 'polls/result.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "you didn't select a choice"
        }
        return render(request, 'polls/detail.html', context)

    choice.votes += 1
    choice.save()

    context = {'question': question}
    return redirect('polls:results', question_id=question_id)
