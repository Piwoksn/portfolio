from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Project, Message
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

class PortalTemplateView(LoginRequiredMixin, ListView):
    template_name = 'portal.html'
    model = Message
    context_object_name = 'messages'

class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'add_project.html'
    model = Project
    fields = ['name', 'short_desc', 'description', 'image1', 'image2', 'image3', 'link']
    context_object_name = 'projects'
    success_url = reverse_lazy('projects')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'add_project.html'
    model = Project
    fields = ['name', 'short_desc', 'description', 'image1', 'image2', 'image3', 'link']
    context_object_name = 'projects'
    success_url = reverse_lazy('projects')

class ProjectTemplateView(LoginRequiredMixin, ListView):
    template_name = 'project.html'
    model = Project
    context_object_name = 'projects'

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('projects')

class MessageDeleteView(DeleteView):
    template_name = 'message_delete.html'
    model = Message
    context_object_name = 'message'
    success_url = reverse_lazy('portal')