from django.urls import path
from . import views 


urlpatterns = [
    path('', views.Professores, name='professores'),
    path('attProf/', views.attProf, name='attProf'),
    path('updateProf/<int:id>', views.updateProf, name='updateProf')
]
