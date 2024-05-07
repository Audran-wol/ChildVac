from django.urls import path
from . import views

app_name = 'vaccination_app'

urlpatterns = [
    path('parent/register/', views.parent_register, name='parent_register'),
    path('parent/login/', views.parent_login, name='parent_login'),
    path('parent/children/', views.child_list, name='child_list'),
    # Add other URL patterns for admin, hospital, and parent sections
]
