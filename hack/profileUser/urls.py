from django.urls import path
from . import views

app_name= "profiles"
urlpatterns = [
    # Other URL patterns...
    path('', views.profile_view, name='profile'),
    path('certifications/', views.certification_list, name='certification_list'),
    path('create/', views.add_certification, name='add_certifications'),
    path('update/<str:pk>', views.update_certification, name='update_certification'),
    path('delete/<str:pk>', views.delete_certification, name='delete_certification'),
]

