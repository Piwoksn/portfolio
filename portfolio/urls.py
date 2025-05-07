from django.urls import path
from .views import HomePageView, ProjectDetailView, message

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('project/<uuid:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('message/', message, name="message"),
]
