from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import MLModel


class MLModelCreateView(LoginRequiredMixin, CreateView):
    model = MLModel
    fields = ['pth_file', 'description']

