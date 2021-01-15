from django.shortcuts import render

def index(request):
    return render(request, 'main/index.htm')

def contact(request):
    return render(request, 'main/contact.htm', {})

def about(request):
    return render(request, 'main/about.htm', {})


# Create your views here.
