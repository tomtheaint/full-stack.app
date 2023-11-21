from django.shortcuts import render

# Create your views here.

#adding task view
from django.http import HttpResponse
from django.template import loader

from .models import Task

def index(request):
    taskList = Task.objects.order_by("name")
    template = loader.get_template("tasks/base.html")
    #output = ", ".join([q.name for q in taskList])
    context = {
        "taskList": taskList,
    }
    return HttpResponse(template.render(context, request))