from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def HomeView(request):
    return render(request, 'home.html')

def MenuView(request):
    return render(request, 'menu.html')

def AboutView(request):
    return render(request, 'about.html')

def BookTableView(request):
    return render(request, 'book_table.html')

def FeedbackView(request):
    return render(request, 'feedback.html')
