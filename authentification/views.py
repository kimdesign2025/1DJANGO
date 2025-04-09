from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Vue pour l'enregistrement d'un utilisateur
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès.")
            return redirect('authentification:login')  # Redirige vers la page de connexion après l'enregistrement
    else:
        form = UserCreationForm()
    
    return render(request, 'authentification/register.html', {'form': form})

# Vue pour la connexion d'un utilisateur
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('produit:dashboard_home_page')  # Redirige vers le dashboard après la connexion
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Formulaire invalide.")
    else:
        form = AuthenticationForm()

    return render(request, 'authentification/login.html', {'form': form})

# Vue pour la déconnexion d'un utilisateur
def logout_view(request):
    logout(request)
    return redirect('produit:home_view')  # Redirige vers la page d'accueil après la déconnexion
