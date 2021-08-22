from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def ps(request):
    return render(request, 'home/ps.html', {'title': 'Process Scheduling'})
