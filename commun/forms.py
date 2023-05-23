from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Benevole
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import DateInput, TimeInput
from .models import Agenda
from django.core.exceptions import ValidationError
from datetime import datetime



class SignupForm(UserCreationForm):
        # choix pour le champ "status"
    CHOICES = [('client', 'Client'), ('benevole', 'Bénévole')]
    # champs du formulaire
    status = forms.ChoiceField(choices=CHOICES)
    email = forms.EmailField(max_length=200, help_text='Requis', label='Email')
    first_name = forms.CharField(max_length=100, help_text='Requis', label='Prénom')
    last_name = forms.CharField(max_length=100, help_text='Requis', label='Nom')
    phone = forms.CharField(max_length=20, help_text='Requis', label='Téléphone')
    address = forms.CharField(max_length=200, help_text='Requis', label='Adresse')

    class Meta:
        # modèle User utilisé pour créer l'utilisateur
        model = User
        # champs du modèle utilisés dans le formulaire
        fields = UserCreationForm.Meta.fields + ('username', 'first_name', 'last_name', 'phone', 'email', 'address', 'password1', 'password2')
        
    def save(self, commit=True):
        # enregistrement de l'utilisateur
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        if commit:
            user.save()
        # enregistrement du profil
        if self.cleaned_data['status'] == 'client':
            client, created = Client.objects.get_or_create(user=user, defaults={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'address': user.address})
        else:
            benevole, created = Benevole.objects.get_or_create(user=user, defaults={'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'phone': user.phone, 'address': user.address})
        return user
    



class agendaForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, label='Email')
    tel = forms.CharField(max_length=20, label='Téléphone')
    date = forms.DateField(label='Date')
    lieu = forms.CharField(max_length=20, label='Lieu')
    heure = forms.TimeField(label='Heure')

    class Meta: 
        model = Agenda
        fields = ['nom_utilisateur', 'date', 'email', 'lieu', 'heure', 'tel', 'commentaire']

