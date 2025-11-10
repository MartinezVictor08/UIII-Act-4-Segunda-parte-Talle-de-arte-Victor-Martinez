from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_TallerdeArte, name='inicio_TallerdeArte'),
    path('agregar_instructor/', views.agregar_instructor, name='agregar_instructor'),
    path('ver_instructor/', views.ver_instructor, name='ver_instructor'),
    path('actualizar_instructor/<int:id>/', views.actualizar_instructor, name='actualizar_instructor'),
    path('realizar_actualizacion_instructor/<int:id>/', views.realizar_actualizacion_instructor, name='realizar_actualizacion_instructor'),
    path('borrar_instructor/<int:id>/', views.borrar_instructor, name='borrar_instructor'),

    path('agregar_material/', views.agregar_material, name='agregar_material'),
    path('ver_material/', views.ver_material, name='ver_material'),
    path('actualizar_material/<int:material_id>/', views.actualizar_material, name='actualizar_material'),
    path('realizar_actualizacion_material/<int:material_id>/', views.realizar_actualizacion_material, name='realizar_actualizacion_material'),
    path('borrar_material/<int:material_id>/', views.borrar_material, name='borrar_material'),

]
