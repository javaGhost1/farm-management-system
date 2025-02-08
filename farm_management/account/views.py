from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':dashboard})

# Create your views here.
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         # validate form
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username = cd['username'], password = cd['password'])

#             # check if user is active
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('User has been successfully logged in')
#                 else:
#                     return HttpResponse('Account has been disabled')
                
#             else:
#                 return HttpResponse("Invalid Username or Pasword")
#     else:
#         form = LoginForm()
    
#     context = {'form':form}
#     return render(request, 'account/login.html', context)