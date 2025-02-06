from django.contrib.auth.models import User

class GestorUsuarios:
    def registrar_usuario(self, nombre, email, password):
        usuario = User.objects.create_user(username=nombre, email=email, password=password)
        usuario.save()

    def validar_membresia(self, usuario_id):
        usuario = User.objects.filter(id=usuario_id).first()
        return usuario is not None