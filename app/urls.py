from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracao/', include('administracao.urls')),
    path('', include('userprofile.urls')),
    path('forum/', include('forum.urls')),
    path('topico/', include('topico.urls')),
    path('resposta/', include('resposta.urls')),
    path('matricula/', include('alunoSubforum.urls')),

]
