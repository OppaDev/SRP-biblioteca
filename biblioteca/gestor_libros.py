from biblioteca.models import Libro

class GestorLibros:
    def agregar_libro(self, titulo, autor, editorial, genero):
        libro = Libro(titulo=titulo, autor=autor, editorial=editorial, genero=genero)
        libro.save()

    def eliminar_libro(self, libro_id):
        Libro.objects.filter(id=libro_id).delete()

    def buscar_libro(self, titulo):
        return Libro.objects.filter(titulo__icontains=titulo)