from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

# ---------------------------
# User Login
# ---------------------------
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')  # Replace 'home' with your main view
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ---------------------------
# User Logout
# ---------------------------
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# ---------------------------
# User Registration
# ---------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')  # Replace 'home' with your main view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
