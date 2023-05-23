from django.shortcuts import render

def index(request):
    welcome_text = "Hello, Django!"
    return render(request, 'index.html', {'welcome_text': welcome_text})
