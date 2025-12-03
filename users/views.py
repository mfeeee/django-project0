from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404

# Create your views here.
def signup(request):
    if request.session.get('user'):
        return redirect('/home/')
    
    status = request.GET.get('status')
    return render(request, 'signup.html', {'status': status})

def login(request):
    if request.session.get('user'):
        return redirect('/home/')
    
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def validate_signup(request):
    if request.session.get('user'):
        return redirect('/home/')
    
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email = email)

    if request.session.get('user'):
        return redirect('/home/')

    if len(user) > 0:
        return redirect('/auth/signup/?status=1')
    
    if len(name.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/signup/?status=2')
    
    if len(password) < 8:
        return redirect('/auth/signup/?status=3')
    
    try:
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User(name = name,
                       email = email,
                       password = password,
                       )
        user.save()
        return redirect('/auth/signup/?status=0')
    except:
        return redirect('/auth/signup/?status=4')

def validate_login(request):
    if request.session.get('user'):
        return redirect('/home/')
    
    email = request.POST.get('email')
    password = request.POST.get('password')
    password = hashlib.sha256(password.encode()).hexdigest()
    users = User.objects.filter(email = email).filter(senha = senha)

    if len(users) == 0:
        return redirect('/auth/login/?status=1')

    if len(users) > 0:
        request.session['user'] = users[0].id
        return redirect('/home/')

def logout(request):
    request.session.flush()
    return redirect('/auth/login/')