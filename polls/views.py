from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Question,Choice
from django.urls import reverse

from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {#传递上下文，将模板当中的变量，映射为python的对象
        'latest_question_list':latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)#替换了以上的两个操作，快捷render函数，载入模板，填充上下文，再返回生成的httpResponse


def detail(request,question_id):
    # try:
    #     #     question = Question.objects.get(pk=question_id)
    #     #     context = {
    #     #         'question':question
    #     #     }
    #     # except Question.DoesNotExist:
    #     #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question':question
    }
    return render(request, 'polls/detail.html',context)


def results(request, question_id):
    question = get_object_or_404(Question,pk=question_id)#根据url中的数字id在Question中查询，返回对应的question实例
    return render(request,'polls/results.html',{'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))




