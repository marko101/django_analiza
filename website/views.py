from django.shortcuts import render
from website.models import Slicice

# Create your views here.
def index(request):
    aplikacije=Slicice.objects.all()
    context = {
        'moja_aplikacija' : aplikacije,
        #'page' : request.path,
        'vidi_ime':request.resolver_match.view_name
    }
    return render(request, 'website/index.html', context)