from biblioteca.models import Prestamo
from django.db.models import Count

class ReporteBiblioteca:
    def generar_reporte_libros(self):
        libros_mas_prestados = Prestamo.objects.values('libro__titulo')\
            .annotate(total_prestamos=Count('libro'))\
            .order_by('-total_prestamos')[:10]
        return libros_mas_prestados

    def generar_reporte_usuarios(self):
        usuarios_frecuentes = Prestamo.objects.values('usuario__username')\
            .annotate(total_prestamos=Count('usuario'))\
            .order_by('-total_prestamos')[:10]
        return usuarios_frecuentes