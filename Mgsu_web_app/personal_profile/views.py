from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    data = {
        'name': "Иван",
        # 'array': 
    }
    return render(request, 'personal_profile/profile.html', data)
    
def logout_view(request):
    logout(request)
    return redirect('../../authorization/pwa')

# def asd(request):
#     return HttpResponse("<h4>dfghjkl</h4>")
