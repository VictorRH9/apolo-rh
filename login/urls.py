from django.urls import path
from .views import login_view, logout_view, inicio_view, empleados_view, calculo_view, historial_view, anticipos_view, configuracion_view

urlpatterns = [
    path('login/',  login_view,  name='login'),
    path('logout/', logout_view, name='logout'),
    path('',           inicio_view,        name='inicio'),
    path('empleados/', empleados_view,     name='empleados'),
    path('calculo/',    calculo_view,      name='calculo'),
    path('historial/',  historial_view,    name='historial'),
    path('anticipos/',  anticipos_view,    name='anticipos'),
    path('configuracion/', configuracion_view, name='configuracion'),
]
