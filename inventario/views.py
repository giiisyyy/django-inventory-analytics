from django.shortcuts import render
from .models import Producto

def panel_inventario(request):
    productos = Producto.objects.all()
    # Filtro algorítmico de stock crítico para el panel de analítica
    stock_critico = productos.filter(stock__lt=5).count()
    
    context = {
        'productos': productos,
        'stock_critico': stock_critico,
    }
    return render(request, 'inventario/panel.html', context)