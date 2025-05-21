from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView, name='Home'),
    path('book_table', BookTableView, name='Book_Table'),
    path('menu', MenuView, name='Menu'),
    path('about', AboutView, name='About'),
    path('feedback', FeedbackView, name='Feedback_Form'),
] 