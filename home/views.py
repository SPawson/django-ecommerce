from django.shortcuts import render

def index(request):
    """Returns index page for site"""
    return render(request, "index.html")
