from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Order, OrderItem
from django.contrib import messages
from .forms import CheckoutForm 
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# --- FUNCIÓN AUXILIAR PARA CONTAR EL CARRITO ---
def get_cart_count(request):
    """Cuenta cuántos artículos en total hay en el carrito"""
    cart = request.session.get('cart', {})
    return sum(cart.values())

# --- VISTA DE INICIO (HOME) ---
def home(request):
    cart_count = get_cart_count(request)
    return render(request, 'store/home.html', {'cart_count': cart_count})

# --- LISTADO DE PRODUCTOS ---
def product_list(request):
    q = request.GET.get('q', '')
    category = request.GET.get('category', '')
    products = Product.objects.all()

    if q:
        products = products.filter(name__icontains=q)
    
    if category:
        products = products.filter(category__iexact=category)

    # Calculamos el carrito
    cart_count = get_cart_count(request)

    return render(request, 'store/product_list.html', {
        'products': products, 
        'q': q, 
        'category': category,
        'cart_count': cart_count  # <--- Enviamos el contador
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_count = get_cart_count(request)
    return render(request, 'store/product_detail.html', {
        'product': product,
        'cart_count': cart_count
    })

# --- CARRITO DE COMPRAS ---
def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for pid_str, qty in cart.items():
        try:
            prod = Product.objects.get(pk=int(pid_str))
        except Product.DoesNotExist:
            continue
        subtotal = prod.price * qty
        items.append({'product': prod, 'quantity': qty, 'subtotal': subtotal})
        total += subtotal
    
    cart_count = get_cart_count(request)
    
    return render(request, 'store/cart.html', {
        'items': items, 
        'total': total,
        'cart_count': cart_count
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    request.session['cart'] = cart
    messages.success(request, "Artículo añadido al carrito.")
    
    # Redirigir a la página anterior o al carrito
    return redirect(request.META.get('HTTP_REFERER', 'store:cart'))

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    key = str(product_id)
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        messages.success(request, "Artículo eliminado del carrito.")
    return redirect('store:cart')

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "El carrito está vacío.")
        return redirect('store:product_list')

    items = []
    total = 0
    for pid_str, qty in cart.items():
        try:
            prod = Product.objects.get(pk=int(pid_str))
        except Product.DoesNotExist:
            continue
        items.append({'product': prod, 'quantity': qty})
        total += prod.price * qty

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                try:
                    order.customer = request.user.customer_profile
                except Customer.DoesNotExist:
                    pass
            order.total = total
            order.save()
            for it in items:
                OrderItem.objects.create(order=order,
                                         product=it['product'],
                                         price=it['product'].price,
                                         quantity=it['quantity'])
            request.session['cart'] = {}
            messages.success(request, f"Pedido creado. ID: {order.id}")
            return redirect('store:orders')
    else:
        form = CheckoutForm()

    cart_count = get_cart_count(request)
    return render(request, 'store/checkout.html', {
        'form': form, 
        'items': items, 
        'total': total,
        'cart_count': cart_count
    })

@login_required
def orders_view(request):
    try:
        customer = request.user.customer_profile
        orders = Order.objects.filter(customer=customer).order_by('-created_at')
    except Customer.DoesNotExist:
        orders = Order.objects.none()
    
    cart_count = get_cart_count(request)
    return render(request, 'store/orders.html', {
        'orders': orders,
        'cart_count': cart_count
    })

# --- VISTA DE CONTACTO ---
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Obtener datos limpios
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject_opt = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Crear el cuerpo del correo
            email_body = f"""
            Nuevo mensaje de contacto de Artesanía Cristiana:
            
            Nombre: {name}
            Email: {email}
            Teléfono: {phone}
            Motivo: {subject_opt}
            
            Mensaje:
            {message}
            """

            # Enviar correo (Simulado a la consola por ahora)
            send_mail(
                subject=f"Contacto Web: {subject_opt}",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['admin@artesaniacristiana.com'], # Correo hipotético
                fail_silently=False,
            )

            # Mensaje de éxito para el usuario
            messages.success(request, "¡Mensaje enviado con éxito! Nos pondremos en contacto contigo en breves.")
            return redirect('store:contact') # Recarga la página limpia
    else:
        form = ContactForm()

    # Calculamos el carrito para que el contador no desaparezca
    # (Si usaste el método de views.py anterior)
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'store/contact.html', {
        'form': form,
        'cart_count': cart_count
    })

