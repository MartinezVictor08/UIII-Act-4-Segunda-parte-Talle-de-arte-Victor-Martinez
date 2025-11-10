from django.contrib import admin
from .models import Instructor, Curso, Material

admin.site.register(Instructor)
admin.site.register(Curso)
admin.site.register(Material)