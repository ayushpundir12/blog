from django.shortcuts import redirect, render
from blogs.models import Category,blog
from assignment.models import About
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
import django.contrib.auth as auth


def home(request):
    categories= Category.objects.all()
    featured_blogs= blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts= blog.objects.filter(status='Published',is_featured=False).order_by('-created_at')
    

    try:
        about=About.objects.get()
    except :
        about=None


    contex={'categories': categories, 
            'featured_blogs': featured_blogs,
             'posts': posts,
             'about': about,}
    return render(request,'home.html',contex)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}! You can now log in.')
            # Optional: automatically log the user in after registration
            # login(request, user)
            return redirect('login')  # Redirect to login page instead of register
        else:
            # Display form errors as messages
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def user_logout(request):
    auth.logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')