# Artesanía Cristiana  
**Práctica 4 – Programación Web con Django**


## 0. Video Funcionalidad

https://www.loom.com/share/0ad93f5ddb1145b883a794f592822309

## 1. Introducción

**Artesanía Cristiana** es una plataforma web desarrollada con Django que combina un sistema de comercio electrónico con una dimensión social y comunitaria. El proyecto no se concibe únicamente como una tienda online, sino como una herramienta de apoyo a la Iglesia y a la juventud, facilitando la recaudación de fondos para misiones, retiros y convivencias.

La aplicación permite la gestión de productos artesanales, pedidos y usuarios, incorporando además elementos interactivos que mejoran la experiencia de usuario.

---

## 2. Filosofía del Proyecto

### 2.1 Misión y Valor Social

Tal como se refleja en la sección institucional de la plataforma, el proyecto nace de un grupo de jóvenes comprometidos con la Iglesia. Su objetivo principal es recaudar fondos destinados a parroquias y conventos, ayudando a financiar actividades formativas y espirituales.

Cada artículo ofrecido (velas, pulseras y llaveros) ha sido diseñado con un enfoque simbólico y espiritual, buscando acompañar e inspirar al usuario en su día a día.

---

### 2.2 Inspiración Visual y Experiencia de Usuario (UI/UX)

La interfaz se ha diseñado siguiendo una estética **minimalista y sacra**, cuidando tanto el aspecto visual como la usabilidad.

- **Banner principal**: Imagen de la Virgen con el Niño, pensada para generar una conexión emocional inmediata.
- **Navegación**: Menú superior limpio con accesos directos a Inicio, Tienda y Contacto, además de áreas específicas para usuarios registrados (Mis pedidos) y administración.
- **Diseño responsive**: Adaptado a dispositivos móviles mediante Bootstrap 5.3.

---

## 3. Arquitectura Técnica

La aplicación está desarrollada siguiendo el patrón **MVT (Modelo–Vista–Template)** de Django, garantizando una separación clara entre:
- Lógica de negocio
- Acceso a datos
- Presentación

### 3.1 Modelo de Datos y Entidades

Las principales entidades del sistema son:


- **Catálogo de Productos**  
  Productos categorizados en *Velas*, *Pulseras* y *Llaveros*.


- **Sistema de Pedidos**  
  Gestión completa de pedidos, desde la selección de productos hasta la confirmación de la compra y su seguimiento.


- **Perfiles de Usuario**  
  Diferenciación entre administradores, vendedores y clientes finales, con permisos y vistas específicas.

---

## 4. Desarrollo Técnico de Funcionalidades

### 4.1 Gestión Dinámica del Carrito de Compras

El carrito de compras se implementa utilizando **Django Sessions**, evitando la creación de registros permanentes en la base de datos hasta que el pedido se confirma.

- En la vista (`views.py`) se accede al carrito mediante:
  ```python
  request.session.get('cart', {})
En la plantilla (cart.html) se utiliza lógica condicional para mostrar el estado del carrito:

```
{% if items %}
    <!-- Mostrar productos -->
{% else %}
    <!-- Carrito vacío -->
{% endif %}
```
Este enfoque permite una gestión eficiente y escalable del carrito.

### 4.2 Chatbot de Asistencia “Maranata”

Se ha desarrollado un chatbot de atención al cliente integrado en base.html, implementado íntegramente en JavaScript, sin necesidad de backend adicional.

Estructura de datos:
Un array de objetos faqData que contiene preguntas y respuestas frecuentes, fácilmente ampliable.

Simulación de inteligencia artificial:
Se implementa un indicador de escritura mediante setTimeout() para simular un comportamiento humano.

Ejemplo de implementación:
```
function handleOptionClick(item) {
    addMessage(item.question, 'user');
    typingIndicator.style.display = 'block';
    setTimeout(() => {
        addMessage(item.answer, 'bot');
    }, 1500);
}

```

### 4.3 Efecto Visual: Lluvia de Cruces

Para reforzar la identidad visual del sitio, se implementa un efecto animado en la vista de listado de productos.

Generación dinámica de elementos DOM mediante setInterval().

Parámetros aleatorios para posición horizontal y velocidad de caída.

Animaciones CSS3 usando @keyframes para traslación vertical y rotación.

Este efecto aporta dinamismo sin afectar significativamente al rendimiento.

### 4.4 Gestión de Formularios y Contacto

El sistema diferencia claramente entre formularios de negocio y formularios informativos:

CheckoutForm (ModelForm)
Vinculado directamente al modelo Order, permitiendo crear pedidos con form.save().

ContactForm (Form)
Formulario independiente con widgets de Bootstrap.
En la vista de contacto se muestra un aviso recomendando el uso previo del chatbot, reduciendo la carga de consultas manuales.

---

# 5. Diseño Responsive y Estilos

La interfaz utiliza Bootstrap 5.3 como base visual.

| Elemento             | Implementación                                               |
| -------------------- | ------------------------------------------------------------ |
| Hero sections        | Imágenes de fondo con overlays semitransparentes             |
| Tarjetas de producto | Sombras dinámicas y efecto `scale` al pasar el cursor        |
| Tablas de pedidos    | Clases `table-hover` y `align-middle` para mayor legibilidad |

---

# 6. Tecnologías Utilizadas

Python 3

Django

HTML5 / CSS3

JavaScript

Bootstrap 5.3

SQLite (entorno de desarrollo)

---

# 7. Conclusión

El proyecto Artesanía Cristiana combina una arquitectura web sólida con una identidad visual cuidada y una clara orientación social. La aplicación demuestra el uso práctico del framework Django para el desarrollo de plataformas web completas, integrando funcionalidades dinámicas, diseño responsive y una experiencia de usuario coherente.
