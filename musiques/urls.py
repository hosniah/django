from django.urls import path
from .views import MorceauDetailView

app_name = 'musiques'


urlpatterns = [
#    path('<int:pk>', morceau_detail, name='morceau-detail')
      path('<int:pk>',MorceauDetailView.as_view(), name='morceau-detail')
]
