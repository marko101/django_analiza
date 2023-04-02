from django.shortcuts import render
from website.models import Slicice

# Create your views here.
def index(request):
    aplikacije=Slicice.objects.all()
    context = {
        'moja_aplikacija' : aplikacije
    }
    return render(request, 'website/index.html', context)