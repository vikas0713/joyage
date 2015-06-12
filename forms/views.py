from django.shortcuts import render_to_response
from forms import RegisterForm
from models import FormsModel as tb
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.

def index(request):
    if request.POST:
        form=RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/result/')
    else:
        form=RegisterForm()
    data={}
    data.update(csrf(request))
    data['form']= form
    return render_to_response('index.html',data)

def result(request):
    data=tb.objects.order_by('created_at').reverse()[:1]
    return render_to_response('result.html',{'data':data})