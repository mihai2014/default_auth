from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("login"))
        else:
            return redirect(reverse("home"))    

    form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})
    
