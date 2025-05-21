from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm

def cadastrar_pedido(request):
    if request.method == 'POST':
        # pedido = Pedido(produto_id=request.POST['produto'], quantidade=request.POST['quantidade'])
        # pedido.save()
        # return redirect('lista_pedidos')
    
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/cadastrar.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})
