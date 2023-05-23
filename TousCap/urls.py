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