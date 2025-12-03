from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Courses, Classes, Comments

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

def classes(request, id):
    if request.session.get('user'):
        classes = Classes.objects.get(id = id)
        user_id = request.session.get('user')
        comments = Comments.objects.filter(classes=classes).order_by('-date')

        return render(request, 'classes.html', {'classes': classes, 'user_id': user_id, 'comments': comments})
    else:
        return redirect('/auth/login/?status=2')

def comments(request):
    user_id = int(request.POST.get('user_id'))
    comment = request.POST.get('comment')
    classes_id = int(request.POST.get('classes_id'))

    comment_instance = Comments(user_id = user_id,
                                comment = comment,
                                classes_id = classes_id)
    comment_instance.save()

    comments = Comments.objects.filter(classes = classes_id).order_by('-date')
    only_names = [i.user.name for i in comments]
    only_comments = [i.comment for i in comments]
    comments = list(zip(only_names, only_comments))

    return HttpResponse(json.dumps({'status': '1', 'comments': comments }))