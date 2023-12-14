from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, User
from . import forms


class SignUpView(View):
    def get(self, request):
        return render(request, 'auth/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

class PasswordChangeView(View):
    def get(self, request):
        return render(request, 'auth/password_change.html')
# class LogInView(View):
#     def get(self, request):
#         return render(request, 'auth/login.html')

# class LoginPageView(View):
#     c
#     form_class = forms.LoginForm
#
#     def get(self, request):
#         form = self.form_class
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')
#         message = 'Login Failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})


# def LoginPageView(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#         else:
#             print("Bunday login mavjud emas")



# def register_user(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("Registration Successfull!"))
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#
#         return render(request, 'auth/register.html', {
#             'form': form,
#         })

class Candidate(View):
    def get(self, request):
        return render(request, 'users/candidate_list.html')

class Userprofile(View):
    def get(self, request):
        return render(request, 'profile/settings.html')