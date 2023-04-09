from django.shortcuts import render

# Create your views here.
def airpolution_welcome(request):
    print('hello')
    context= {
        #'page': request.path
        'vidi_ime':request.resolver_match.view_name
    }
    return render(request, 'airpolution/welcome.html', context)