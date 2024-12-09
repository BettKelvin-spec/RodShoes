from django.shortcuts import render
from .models import Shoe

# Create your views here.
def index(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {'shoes': shoes})

