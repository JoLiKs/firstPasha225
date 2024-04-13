from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from app.models import Users


@csrf_exempt
def register(request):
    if request.method == 'POST':
        login = request.POST['login']
        email = request.POST['email']
        for i in Users.objects.all():
            if i.email == email:
                return render(request, 'reg.html', {'msg': 'Данный Email занят!'})
            if i.login == login:
                return render(request, 'reg.html', {'msg': 'Данный логин занят!'})
        user = Users()
        user.email = email
        user.name = request.POST['name']
        user.login = login
        user.password = request.POST['password']
        user.save()
        html = redirect('/profile/')
        html.set_cookie('email', email)
        html.set_cookie('name', f"{request.POST['name']}")
        return html
    return render(request, 'reg.html')


def index(request):
  return render(request, 'index.html')


@csrf_exempt
def login(request):
    if len(request.COOKIES.items()) > 1:
        return redirect('/profile/')
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        for i in Users.objects.all():
            if i.login == login and i.password == password:
                print('Auth succ')
                html = redirect('/profile/')
                html.set_cookie('email', i.email)
                html.set_cookie('name', i.name)
                return html
        return render(request, 'login.html', {'msg': 'Неверный логин или пароль'})
    return render(request, 'login.html')


@csrf_exempt
def абракадабра(request):
    if request.method == 'POST':
        html = redirect('/')
        html.delete_cookie('email')
        html.delete_cookie('name')
        return html
    try:
        if not request.COOKIES['email'] is None:
            return render(request, 'profile.html', {"email":request.COOKIES['email'], "name": request.COOKIES['name']})
    except Exception as e:
        print("Error:", e)
        return redirect('/')

