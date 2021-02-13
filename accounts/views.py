from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.views import LoginView as SignUp
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import MyUser
from .forms import UserForm, UserProfile


from django.contrib import auth

class HomePageView(TemplateView):
    template_name = 'home.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=True)
            
            # cleaned (normalized) data
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            

            user.set_password(password)

            user.save()

            # returns user objects if credentials are correct

            user = authenticate(email=email, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('accounts:home')

            return render(request, self.template_name, {'form': form.as_p})



class LoginView(SignUp):
    template_name = 'registration/login.html'

    def connect(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('accounts:home')
        else:
            return redirect('accounts:register')

class logoutView(LogoutView):
    template_name = 'registration/logged_out.html'

    def disconnect(self, request):
        logout(request)
        return redirect('accounts:logout')

class ProfileView(View):
    form_class = UserForm
    template_name = 'registration/profile.html'

    def get(self, request):
        user = request.user
        context = { 'user': user}
        return render(request, self.template_name, context)

class ProfileUpdate(UpdateView):
    moddel = MyUser
    #fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'gender', 'city']
    form_class = UserProfile


    def get_object(self, queryset=None):
        return self.request.user






