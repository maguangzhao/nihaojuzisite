from django.shortcuts import render
from .models import JuZi,Book
from django.views.generic import ListView,DetailView

# Create your views here.
class JuZiListView(ListView):
    queryset = JuZi.objects.all()
    context_object_name = 'juzis'
    paginate_by = 5
    template_name = 'blog/juzi/juzilist.html'

