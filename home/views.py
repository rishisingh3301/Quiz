from django.shortcuts import render, HttpResponse #HttpResponse is added manually

#added manually
from .models import registration

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # context={
    #     "var1":"RISHI IS VARIABLE 1",
    #     "var2":"ABHAY IS VARIABLE 2",
    # }
    
    # return render(request, 'index.html', context)
    # return HttpResponse("THIS IS HOME PAGE AND IT IS WHAT IT IS!")
    
# nameview = ""
# emailview = ""
# gradeview = ""
# stateview = ""
# aboutview = ""

def club(request):
    return render(request, 'club.html')
def contact(request):
    return render(request, 'contact.html')
def auction(request):
    return render(request, 'auction.html')
def esummit(request):
    return render(request, 'esummit.html')

def points(request):
    if request.method == "POST":
        pointview1 = request.POST.get('q1')
        pointview2 = request.POST.get('q2')
        pointview3 = request.POST.get('q3')
        pointview4 = request.POST.get('q4')
        pointview5 = request.POST.get('q5')
        x=0
        if pointview1=="Apple":
            x=x+1
        if pointview2=="Earth":
            x=x+1
        if pointview3=="4":
            x=x+1
        if pointview4=="West Bengal":
            x=x+1
        if pointview5=="60":
            x=x+1
        
        

        variable = registration(name = question.nameview, email = question.emailview, grade = question.gradeview, state = question.stateview, about = question.aboutview, score=x)
    
        variable.save()

        print("WORKING")

        return render(request, 'points.html', {"score":x} )

def question(request):
    if request.method == "POST":
        question.nameview = request.POST.get('htmlname')
        question.emailview = request.POST.get('htmlemail')
        question.gradeview = request.POST.get('htmlgrade')
        question.stateview = request.POST.get('htmlstate')
        question.aboutview = request.POST.get('htmlabout')
        

        
        return render(request, 'question.html')

def quiz(request):

    return render(request, 'quiz.html')
