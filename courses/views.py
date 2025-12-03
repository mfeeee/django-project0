from django.shortcuts import render, redirect
from .models import Courses, Classes

# Create your views here.
def home(request):
    if request.session.get('user'):
        courses = Courses.objects.all()
        request_user = request.session.get('user')
        return render(request, 'home.html', {'courses': courses, 'request_user': request_user})
    else:
        return redirect('/auth/login/?status=2')

def course(request, id):
    if request.session.get('user'):
        classes = Classes.objects.filter(course = id)
        request_user = request.session.get('user')
        return render(request, 'course.html', {'classes': classes, 'request_user': request_user})
    else:
        return redirect('/auth/login/?status=2')
