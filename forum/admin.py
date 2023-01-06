from django.contrib import admin
from forum.models import Categoria, Subforum, Topico

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Subforum)
admin.site.register(Topico)