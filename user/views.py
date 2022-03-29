from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm, UserForm


@login_required
def perfil(request):
    informacoes = Usuario.objects.filter(user=request.user)
    context = {'informacoes': informacoes}
    return render(request, 'user/perfil.html', context)


def cadastro(request):
    if request.method != 'POST':
        user_form = UserForm()
        usuario_form = UsuarioForm()
    else:
        user_form = UserForm(request.POST, instance=request.user)
        usuario_form = UsuarioForm(request.POST, instance=request.user.usuario)
        if user_form.is_valid() and usuario_form.is_valid():
            user_form.save()
            usuario_form.save()
            return redirect('perfil')

    context = {'user_form': user_form, 'usuario_form': usuario_form}
    return render(request, 'user/cadastro.html', context)
