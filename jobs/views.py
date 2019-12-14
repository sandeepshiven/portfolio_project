from django.shortcuts import render
from .models import Job
from .models import Project
# Create your views here.

def home(request):
    jobs = Job.objects
    projects = Project.objects
    return render(request, 'jobs/home.html',{"jobs":jobs,"projects":projects})

