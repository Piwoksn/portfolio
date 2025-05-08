from django.urls import path
from .views import HomePageView, ProjectDetailView, message, PortalTemplateView, ProjectAddView, ProjectUpdateView, ProjectTemplateView, ProjectDeleteView, MessageDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('project/<uuid:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_update/<uuid:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project_delete/<uuid:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('message_delete/<str:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('projects/', ProjectTemplateView.as_view(), name='projects'),
    path('portal/', PortalTemplateView.as_view(), name='portal'),
    path('addproject/', ProjectAddView.as_view(), name='add_project'),
    path('message/', message, name="message"),
]
