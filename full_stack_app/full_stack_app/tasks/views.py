from django.shortcuts import render

# Create your views here.

#adding task view
from django.http import HttpResponse
from django.template import loader

from .models import Task


#def display_tasks(request):
#    tasks = Task.objects.all()
#    template = loader.get_template("tasks/base.html")
#    #return render(request, "display_tasks.html", {"tasks": tasks})
#    return HttpResponse(template.render(request), {})

#def index(request):
#    print(request.htmx)
#    
#    if request.htmx:
#        print("HTMX Request")
#    else:
#        print("Non-HTMX Request")
#    return render(request, 'tasks/base.html')

def index(request):
    taskList = Task.objects.order_by("name")
    template = loader.get_template("pages/home.html")
    #output = ", ".join([q.name for q in taskList])
    context = {
        "taskList": taskList,
    }
    return HttpResponse(template.render(context, request))