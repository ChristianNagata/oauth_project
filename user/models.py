from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    criado_em = models.DateField(auto_now=True)

    @receiver(post_save, sender=User)
    def criar_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def salvar_usuario(sender, instance, **kwargs):
        instance.usuario.save()


class UsuarioChefe(Usuario):
    """Usuário que fez a compra do plano."""
    plano_expira_em = models.DateTimeField()


class UsuarioComum(Usuario):
    """
    Usuário convidado por quem fez a compra.
    Será deletado em 4 casos:
        1. Se 'User' for deletado;
        2. se 'UsuarioChefe' for deletado;
        3. se por algum usuário com permissões de deletar;
        4. se deletar a própria conta.
    """
    chefe = models.ForeignKey(UsuarioChefe, on_delete=models.CASCADE)


class Perfil(models.Model):
    usuario = models.ForeignKey(UsuarioComum, on_delete=models.CASCADE)


class Permissao(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    editar_permissoes = models.BooleanField(default=False)
    deletar_usuarios = models.BooleanField(default=False)
    criar_propriedades = models.BooleanField(default=False)
    acessar_balanco = models.BooleanField(default=False)
    enviar_convites = models.BooleanField(default=False)
