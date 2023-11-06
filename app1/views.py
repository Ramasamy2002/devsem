from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import table1
from django.views.decorators.csrf import csrf_exempt
def sample(request):
    return HttpResponse("hello world")
def htmlren(request):
    template=loader.get_template('sample.html')
    return HttpResponse(template.render())
def index(request):
    data=table1.objects.all()
    return render(request,'index.html',{'data':data})
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render())
@csrf_exempt
def addrecord(request):
    x=request.POST["first"]
    y=request.POST["last"]
    z=request.POST["roll"]
    t=table1(firstname=x,lastname=y,roll=z)
    t.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    t=table1.objects.get(id=id)
    t.delete()
    return HttpResponseRedirect(reverse('index'))




