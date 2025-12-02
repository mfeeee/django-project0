from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import Http404

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return ender(request, 'login.html')

def validate_signup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email = email)

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
