from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

'''def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'registration', {'form': form})'''

def first(request):
    return render(request, 'authorization/first.html')

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('../timetable')  # Перенаправляем на главную страницу
    
    return render(request, 'authorization/auth.html', {'form': form})