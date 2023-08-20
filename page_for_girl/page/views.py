from django.shortcuts import render, redirect

def stream(request):
    return render(request, "page/index.html")