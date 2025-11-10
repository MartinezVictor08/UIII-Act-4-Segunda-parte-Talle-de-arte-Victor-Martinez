from django.shortcuts import render, redirect
from .models import Instructor

# Página de inicio
def inicio_TallerdeArte(request):
    return render(request, 'inicio.html')


# Agregar instructor
def agregar_instructor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        correo = request.POST['correo']
        experiencia_anios = request.POST['experiencia_anios']
        sueldo = request.POST['sueldo']

        nuevo = Instructor(
            nombre=nombre,
            apellido=apellido,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo,
            experiencia_anios=experiencia_anios,
            sueldo=sueldo
        )
        nuevo.save()
        return redirect('ver_instructor')
    return render(request, 'instructor/agregar_instructor.html')


# Ver instructores
def ver_instructor(request):
    instructores = Instructor.objects.all()
    return render(request, 'instructor/ver_instructor.html', {'instructores': instructores})


# Actualizar instructor
def actualizar_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    return render(request, 'instructor/actualizar_instructor.html', {'instructor': instructor})


# Realizar actualización
def realizar_actualizacion_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    if request.method == 'POST':
        instructor.nombre = request.POST['nombre']
        instructor.apellido = request.POST['apellido']
        instructor.especialidad = request.POST['especialidad']
        instructor.telefono = request.POST['telefono']
        instructor.correo = request.POST['correo']
        instructor.experiencia_anios = request.POST['experiencia_anios']
        instructor.sueldo = request.POST['sueldo']
        instructor.save()
        return redirect('ver_instructor')
    return redirect('ver_instructor')


# Borrar instructor
def borrar_instructor(request, id):
    instructor = Instructor.objects.get(instructor_id=id)
    instructor.delete()
    return redirect('ver_instructor')




from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
# Si usas Curso luego, puedes importarlo: from .models import Curso

# Agregar material
def agregar_material(request):
    if request.method == 'POST':
        nombre_material = request.POST.get('nombre_material')
        tipo = request.POST.get('tipo')
        marca = request.POST.get('marca')
        cantidad_stock = request.POST.get('cantidad_stock') or 0
        costo_unitario = request.POST.get('costo_unitario') or 0
        nombre_proveedor = request.POST.get('nombre_proveedor')
        descripcion = request.POST.get('descripcion')
        # si tienes curso y recibes id del curso:
        curso_id = request.POST.get('curso')  # opcional
        if curso_id:
            try:
                from .models import Curso
                curso_obj = Curso.objects.get(pk=curso_id)
            except Exception:
                curso_obj = None
        else:
            curso_obj = None

        Material.objects.create(
            nombre_material=nombre_material,
            tipo=tipo,
            marca=marca,
            cantidad_stock=cantidad_stock,
            costo_unitario=costo_unitario,
            nombre_proveedor=nombre_proveedor,
            descripcion=descripcion,
            curso=curso_obj
        )
        return redirect('ver_material')
    return render(request, 'material/agregar_material.html')

# Ver materiales (lista)
def ver_material(request):
    materiales = Material.objects.all().order_by('material_id')
    return render(request, 'material/ver_material.html', {'materiales': materiales})

# Mostrar formulario de actualización
def actualizar_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    return render(request, 'material/actualizar_material.html', {'material': material})

# Procesar actualización
def realizar_actualizacion_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        material.nombre_material = request.POST.get('nombre_material')
        material.tipo = request.POST.get('tipo')
        material.marca = request.POST.get('marca')
        material.cantidad_stock = request.POST.get('cantidad_stock') or 0
        material.costo_unitario = request.POST.get('costo_unitario') or 0
        material.nombre_proveedor = request.POST.get('nombre_proveedor')
        material.descripcion = request.POST.get('descripcion')
        # curso opcional
        curso_id = request.POST.get('curso')
        if curso_id:
            try:
                from .models import Curso
                material.curso = Curso.objects.get(pk=curso_id)
            except Exception:
                material.curso = None
        material.save()
        return redirect('ver_material')
    return redirect('ver_material')

# Borrar material (confirmación y borrado)
def borrar_material(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_material')
    return render(request, 'material/borrar_material.html', {'material': material})