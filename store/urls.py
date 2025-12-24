from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # 1. PÁGINA DE INICIO (Raíz): Muestra "Quiénes somos" y la imagen
    path('', views.home, name='home'),

    # 2. TIENDA (Catálogo): Aquí se listan los productos y funcionan los filtros
    path('tienda/', views.product_list, name='product_list'),

    # --- El resto de rutas se mantienen igual ---
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders_view, name='orders'),
    path('contacto/', views.contact_view, name='contact'),
]
