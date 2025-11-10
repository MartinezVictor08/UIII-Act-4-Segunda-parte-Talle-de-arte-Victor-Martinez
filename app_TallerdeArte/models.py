from django.db import models

# ==========================================
# MODELO: INSTRUCTOR
# ==========================================
class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    experiencia_anios = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: CURSO
# ==========================================
class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    salon_num = models.IntegerField()
    duracion_semanas = models.PositiveIntegerField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_inicio = models.DateField()
    cupo_maximo = models.PositiveIntegerField()

    # Relación 1:M (un instructor puede tener muchos cursos)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre_curso


# ==========================================
# MODELO: MATERIAL
# ==========================================
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    nombre_material = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    cantidad_stock = models.PositiveIntegerField()
    costo_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    nombre_proveedor = models.CharField(max_length=100)
    descripcion = models.TextField()

    # Relación 1:M (un curso puede tener muchos materiales)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE, related_name='materiales', null=True, blank=True)


    def __str__(self):
        return self.nombre_material