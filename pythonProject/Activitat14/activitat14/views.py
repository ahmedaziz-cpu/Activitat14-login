from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from .forms import createUserForm
from .models import Usuario


def index(request):
    return render(request,'index.html')


def paginaIncial(request):
    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    return render(request, 'PaginaLogin.html', {'usuario':usuario})



def loggin_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = Usuario.objects.get(username=username)
            if check_password(password, user.password):
                request.session['usuario_id'] = user.id
                return redirect('paginaIncial')
            else:
                error = 'Contraseña incorrecta'
        except Usuario.DoesNotExist:
            error = 'Usuario no encontrado'

        return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def create_user(request):
    success = False
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(form.cleaned_data['password'])  # Cifrar contraseña si no no me deja, PUNTO MUY IMPORTANTE
            usuario.save()
            success = True
    else:
        form = createUserForm()

    return render(request, 'CreateUser.html', {'form': form, 'success': success})