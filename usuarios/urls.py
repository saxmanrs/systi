from django.urls import path
from .views import u_list

urlpatterns = [
    path('listar/',u_list),
]
