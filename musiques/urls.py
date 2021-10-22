from django.urls import path
from .views import morceau_detail

app_name = 'musiques'

urlpatterns = [
    path('<int:pk>', morceau_detail, name='morceau-detail')
]
