from django.shortcuts import render


def index(request):
    return render(request, 'frontend/index.html')


def streams(request):
    return render(request, 'frontend/streams.html')
