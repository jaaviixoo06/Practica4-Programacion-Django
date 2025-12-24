from django import forms
from .models import Order

# ==========================================
# 1. FORMULARIO DE PAGO (CHECKOUT) - (El que faltaba)
# ==========================================
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'phone', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre y Apellidos'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de contacto'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa de envío'}),
        }

# ==========================================
# 2. FORMULARIO DE CONTACTO
# ==========================================
class ContactForm(forms.Form):
    SUBJECT_CHOICES = [
        ('', 'Selecciona un motivo...'),
        ('pedido', 'Problema con mi pedido'),
        ('info', 'Información sobre productos'),
        ('envio', 'Consulta sobre envíos'),
        ('otro', 'Otro motivo'),
    ]

    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre completo'})
    )
    phone = forms.CharField(
        max_length=20, 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu teléfono (opcional)'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tuemail@ejemplo.com'})
    )
    subject = forms.ChoiceField(
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 5, 
            'placeholder': 'Cuéntanos qué ocurre (máx 500 caracteres)...'
        }),
        max_length=500,
        help_text="Límite de 500 caracteres."
    )