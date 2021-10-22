from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Morceau

# Create your views here.

class MorceauDetailView(DetailView):
    model = Morceau
