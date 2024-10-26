from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
users = ['user1','user2']
def user_valid(**kwargs):
    err = []
    if kwargs['username'] in users:
        err.pop('Пользователь уже существует')
    if kwargs['password']!=kwargs['repeat_password']:
        err.pop('Пароли не совпадают')
    if int(kwargs['age']) < 18:
        err.pop('Вы должны быть старше 18')
    return err

def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        age = request.POST.get('age')
        err = user_valid(username=username,repeat_password=repeat_password,password=password,age=age)
        info['len_error'] = len(err)
        if len(err) == 0:
            return HttpResponse(f'Приветствуем {username}!')
        else:
            info['error'] = err
            return HttpResponse(info)
    info['formtype'] = 'html'
    return render(request,'fifth_task/registration_page.html', context= info)
# Create your views here.
def sign_up_by_django(request):
    info = {}
    err = []
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            err = user_valid(username=username, repeat_password=repeat_password, password=password, age=age)
            if len(err) == 0:
                return HttpResponse(f'Приветствуем {username}!')
            else:
                info['error'] = err
                return HttpResponse(info)
        else:
            form = UserRegister()
        info['form'] = form
        info['formtype'] = 'django'
        info['len_error'] = len(err)
        return render(request,'fifth_task/registration_page.html', context=info)
