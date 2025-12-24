# store/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    store_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.store_name or self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pulsera', 'Pulsera'),
        ('llavero', 'Llavero'),
	('vela', 'Velas'),
        ('otro', 'Otro'),
    ]
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='otro')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

ORDER_STATUS = [
    ('pending', 'Pendiente'),
    ('processing', 'En proceso'),
    ('shipped', 'Enviado'),
    ('completed', 'Completado'),
    ('cancelled', 'Cancelado'),
]

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido {self.id} - {self.full_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
