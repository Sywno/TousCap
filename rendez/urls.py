"""rendez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from commun.views import signup, home, agenda, logout_user, login_user, liste_rendez_vous, agenda_detail, mes_missions,supprimer_mission, equipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('agenda/', agenda, name='agenda'),
    path('logout/', logout_user, name='logout'),
    path('liste_rendez_vous/', liste_rendez_vous, name ='liste_rendez_vous'),
    path('mission/<int:agenda_id>/', agenda_detail, name='mission'),
    path('mes_missions/', mes_missions, name='mes_missions'),
    path('supprimer_mission/<int:agenda_id>/', supprimer_mission, name='supprimer_mission'),
    path('equipe/', equipe, name='equipe'),
]
