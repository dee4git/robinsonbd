from django.shortcuts import render


def home(request):
    """shows the home content"""
    return render(request, 'index.html')
