from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "evenements"
urlpatterns = [
    path('', views.liste_evenements, name='liste_evenements'),
    path('evenement/<int:pk>/join/', views.join_event, name='join_event'),
]
