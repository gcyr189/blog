from django.shortcuts import render
from django.utils import timezone
from .models import Fotos

# Create your views here.
def post_list(request):
    posts = Fotos.objects.order_by('fecha')
    return render(request, 'blog/post_list.html', {'fotos':posts})
