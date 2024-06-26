from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from .utils import generate_short_url
from .forms import URLForm
from .models import URL
from django.views.decorators.http import require_http_method


def home(request):
    if request.user.is_authenticated:
        return redirect('shorten_url')
    else:
        return redirect('login')

def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            short_url = generate_short_url()
        try:
            url_object = URL.objects.get(short_url=short_url)
            original_url = url_object.original_url
            return render(request, 'retrieve_url.html', {'original_url': original_url})
        except URL.DoesNotExist:
             # Handle case where the short URL is not found
            error_message = 'Shortened URL not found'
            return render(request, 'retrieve_url.html', {'error_message': error_message})
    else:
        form = URLForm()
    return render(request, 'shorten_url.html', {'form': form})


    


def retrieve_url(request):
    if request.method == 'POST':
        short_url = request.POST.get('short_url')
        try:
            url_object = URL.objects.get(short_url=short_url)
            original_url = url_object.original_url
            return render(request, 'retrieve_url.html', {'original_url': original_url})
        except URL.DoesNotExist:
             # Handle case where the short URL is not found
            error_message = 'Shortened URL not found'
            return render(request, 'retrieve_url.html', {'error_message': error_message})
    else:
        return render(request, 'retrieve_url.html')


def redirect_original(request, short_url):
    try:
        url_obj = URL.objects.get(short_url=short_url)
        return redirect(url_obj.original_url)
    except URL.DoesNotExist:
        # Handle case where the short URL is not found
        return render(request, 'error.html', {'error_message': 'Shortened URL not found'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shorten_url')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'logout.html')
    else:
        return redirect('login')
