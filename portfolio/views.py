
from django.views.generic import ListView
from .models import Project, Resume

class HomePageView(ListView):
    model = Project
    template_name = 'home.html'

class DocumentView(ListView):
    model = Resume
    template_name = 'resume.html'