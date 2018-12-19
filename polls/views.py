from django.shortcuts import reverse

from django.shortcuts import render, get_object_or_404

from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.views import generic

from .models import Question, Choice
from django.template import loader
from django.http import Http404


"""
def index(request):

    latest_question_list = Question.objects.order_by('-publish_date')[:5]

    template = loader.get_template('polls/index.html')

    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ','.join([q.question_text for q in latest_question_list])

    return HttpResponse(template.render(context, request))


def detail(request, question_id):

    # return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    #
    # except Question.DoesNotExist:
    #
    #     raise Http404("Question does not exist !")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    # response = "You're looking at the results of question %s."

    # return HttpResponse(response % question_id)

    #此处有一个bug，pk写成pK了。
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})

"""

class IndexView(generic.ListView):

    template_name = 'polls/index.html'

    context_object_name = 'latest_question_list'


    def get_queryset(self):

    #返回最近发布的5个问卷.

        return Question.objects.order_by('-publish_date')[:5]



class DetailView(generic.DetailView):

    model = Question

    template_name = 'polls/detail.html'



class ResultsView(generic.DetailView):

    model = Question

    template_name ='polls/results.html'



def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:

        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",

        })

    else:

        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # return HttpResponse("You're voting on question %s." % question_id)



