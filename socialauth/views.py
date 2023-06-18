from django.http import HttpResponse
from django.shortcuts import render, redirect

def profile(request):
    return HttpResponse("Fiti")

def home(request):
    if request.user.is_authenticated:
        return HttpResponse('Welcome')
    else:
        return render(request, 'pages/Homepage.html')
        

# def home(request):
#     return render(request, 'pages/Homepage.html',)

#     # Redirect the user to the Google OAuth consent screen
#     return redirect('https://accounts.google.com/o/oauth2/auth?response_type=code&scope=email \
#                     profile&client_id=24809060874-p4kr6f002j9kmccvkbi490tull39s1t3.apps.googleusercontent.com \
#                     &redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/ &approval_prompt=force')


