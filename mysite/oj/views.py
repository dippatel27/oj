from django.shortcuts import render


from django.http import HttpResponse
#from django.template import loader


#from django.http import Http404

from django.shortcuts import get_object_or_404, render

from oj.models import  Question,user,Submissions,TestCases
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('oj/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'oj/index.html', context)
   
    


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'oj/detail.html', {'question': question})