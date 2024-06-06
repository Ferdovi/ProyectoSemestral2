from django.shortcuts import render, redirect
from .forms import * # Importar el formulario de productos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import *
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def ordenlista(request):
    ordenes = Orden.objects.all()
    return render(request, 'core/ordenlista.html',{'ordenes': ordenes})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombreUsuario = form.cleaned_data.get('usuario')
            contrasenaUsuario = form.cleaned_data.get('contraseña')
            user = authenticate(usuario=nombreUsuario, contraseña=contrasenaUsuario)
            if user is not None:
                login(request, user)
                return redirect('ruta_despues_de_iniciar_sesion')  # Redirige a una página específica después de iniciar sesión
    else:
        form = AuthenticationForm()
    
    return render(request, 'nombre_de_tu_template.html', {'form': form})

def orden(request):
    
    if request.method == 'POST':
        formulario_orden = OrdenForm(request.POST)

        if formulario_orden.is_valid():
            orden = formulario_orden.save(commit=False)
            orden.save()  # Guardar la orden para obtener un ID
            
            # Obtener los productos asociados a la orden
            productos_orden = orden.productos.all()
            
            subtotal = 0
            
            # Calcular el subtotal sumando el precio total de cada producto
            for producto in productos_orden:
                subtotal += producto.precio_unitario * producto.cantidad
            
            # Calcular el IVA y el total
            iva = subtotal * 0.19
            total = subtotal + iva

            orden.iva = iva
            orden.total = total

            orden.save()  # Guardar la orden nuevamente con los valores actualizados
            formulario_orden.save_m2m()

            messages.success(request, "Orden creada correctamente")
            return redirect('index')  
        else:
            messages.error(request, "Error al crear la orden")

    else:
        formulario_orden = OrdenForm()

    aux = {
        'form': formulario_orden,
        'msj': ''
    }
    return render(request, 'core/orden.html', aux)



def login(request):
    return render(request, 'core/login.html')

def producto(request):
    if request.method == 'POST':
        formularioproducto = ProductoForm(request.POST)

        if formularioproducto.is_valid():
            # Asigna los IDs al formulario de orden
            formularioproducto.save()

            messages.success(request, "Producto creado correctamente")
            return redirect('producto')  
        else:
            messages.error(request, "Error al crear la orden")

    else:
        formularioproducto = ProductoForm()

    aux = {
        'form': formularioproducto,
        'msj': ''  # Inicializa la variable 'msj' con un valor vacío
    }
    return render(request, 'core/producto.html', aux)

