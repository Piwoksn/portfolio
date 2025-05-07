from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Project, Message
from django.contrib import messages

# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio-details.html'
    context_object_name = 'project'

def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        new_message = Message(
            name= name,
            email = email,
            subject = subject,
            message=message
        )
        new_message.save()
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect('/#contact')
    else:
        return render(request, 'index.html')
    
    return render(request, 'index.html', {'messages': messages})