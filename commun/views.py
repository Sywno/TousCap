from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import agendaForm
from .models import Agenda
from django.contrib.auth.decorators import user_passes_test
from commun .models import Benevole
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.translation import activate

def supprimer_mission(request, agenda_id):
    if request.method == 'POST':
        agenda_item = get_object_or_404(Agenda, id=agenda_id)
        if agenda_item.user == request.user:
            agenda_item.delete()
            messages.success(request, 'Mission validée et supprimée avec succès.')
        else:
            messages.error(request, 'Une erreur est survenue.')
        return redirect('mes_missions')
    else:
        return redirect('mes_missions')

def mes_missions(request):
    user = request.user
    user_agendas = Agenda.objects.filter(user=user)
    return render(request, 'commun/mes_missions.html', {'user_agendas': user_agendas}) 

from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Inscription réussie. Vous êtes maintenant connecté.")
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    # Ajout de la traduction des messages d'erreur
                    if field == 'first_name':
                        messages.error(request, "Prénom : {}".format(error))
                    elif field == 'last_name':
                        messages.error(request, "Nom : {}".format(error))
                    else:
                        messages.error(request, "{} : {}".format(field, error))
    else:
        form = SignupForm()
        activate('fr')  # Activation de la traduction française

    return render(request, 'commun/signup.html', {'form': form})




def home(request):
    return render(request, 'commun/home.html')

def equipe(request):
    return render(request,'commun/equipe.html')


def agenda(request):
    if request.method == 'POST':
        form = agendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = agendaForm()
    return render(request, 'commun/agenda.html', {'form':form})


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('home')
            elif hasattr(user, 'benevole_profile'):
                return redirect('home')
            elif hasattr(user, 'client_profile'):
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'Le nom d\'utilisateur ou le mot de passe est incorrect.')
    
    return render(request, 'commun/login.html')
'''
def est_benevole(user):
    return Benevole.objects.filter(name="Benevole", user=user).exists()
    

@user_passes_test(est_benevole)'''
def liste_rendez_vous(request,):
    rendez_vous = Agenda.objects.filter(user__isnull=True)
    return render(request, 'commun/liste_rendez_vous.html', {'rendez_vous' : rendez_vous})

def agenda_detail(request, agenda_id):
    agenda_item = get_object_or_404(Agenda, id=agenda_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Valider':
            if agenda_item.user is not None:
                messages.error(request, 'Cette mission a déjà été prise.')
                return redirect('liste_rendez_vous')
            else:
                agenda_item.user = request.user
                agenda_item.save()
                messages.success(request, 'Mission validée avec succès.')
                return redirect('liste_rendez_vous')
        elif action == 'Retour':
            # Ici, vous pouvez gérer l'action de refus. Par exemple, vous pouvez supprimer la mission :
            return redirect('liste_rendez_vous')
    else:
        context = {'agenda_item': agenda_item}
        return render(request, 'commun/mission.html', context)