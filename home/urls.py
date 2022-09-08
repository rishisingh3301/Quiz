#everything added manually
from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "EDC Admin"
admin.site.site_title = "EDC Admin Portal"
admin.site.index_title = "Welcome to EDC Portal"

urlpatterns = [
    path('',views.index, name='HOME'),
    path('edc',views.index, name='HOME'),
    path('club',views.club, name='club'),
    path('contact',views.contact, name='contact'),
    path('quiz',views.quiz, name='quiz'),
    path('auction',views.auction, name='auction'),
    path('esummit',views.esummit, name='esummit'),
    path('points',views.points, name='points'),
    path('question',views.question, name='question'),
]
