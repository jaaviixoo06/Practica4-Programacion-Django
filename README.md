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

## 4. Documentación de las funcionalidades implementadas

### 4.1️ Modelos de datos (Models)

El sistema se apoya en varios modelos principales que representan las entidades fundamentales de la aplicación:

Seller: representa al vendedor o responsable del servicio, asociado a un usuario de Django.

Customer: representa al cliente que realiza compras en la tienda.

Product: representa los artículos disponibles en la tienda.
Incluye información como nombre, descripción, precio, stock, categoría, imagen y un slug para generar URLs amigables.

Order: representa un pedido realizado por un cliente, incluyendo su estado (pendiente, procesado, enviado, etc.), el total y la fecha de creación.

OrderItem: representa cada producto incluido dentro de un pedido, almacenando cantidad y precio en el momento de la compra.

Estos modelos están relacionados mediante claves externas (ForeignKey), permitiendo reflejar correctamente las relaciones cliente–pedido y pedido–productos.


### 4.2️ Vistas (Views)

Las vistas implementadas siguen el patrón MVT de Django y se encargan de gestionar la lógica del backend:

home: muestra la página principal con información general del proyecto.

product_list: consulta la base de datos y muestra el catálogo completo de productos disponibles.

product_detail: muestra el detalle de un producto concreto, incluyendo imagen, descripción, precio, categoría y stock.

add_to_cart / remove_from_cart: permiten añadir y eliminar productos del carrito de compra.

cart_view: muestra el contenido actual del carrito.

checkout: gestiona la finalización de la compra y la creación del pedido.

orders_view: permite al cliente consultar el estado de sus pedidos realizados.

contact_view: muestra un formulario de contacto básico.

Todas las vistas realizan consultas dinámicas a la base de datos y envían la información necesaria a los templates HTML.

### 4.3️ Rutas y navegación (URLs)

El archivo urls.py define rutas claras y semánticas para la aplicación:

/ → Página de inicio

/tienda/ → Catálogo de productos

/product/<slug>/ → Detalle de un producto

/cart/ → Carrito de compra

/checkout/ → Finalización del pedido

/orders/ → Consulta de pedidos del cliente

El uso de slugs mejora la legibilidad de las URLs y la experiencia de usuario.

### 4️.4 Templates HTML

Los templates están desarrollados utilizando HTML y Bootstrap 5 para garantizar un diseño responsive y moderno.

Ejemplo de funcionalidades implementadas en los templates:

Visualización dinámica de productos desde la base de datos.

Página de detalle de producto con imagen, precio, categoría y stock.

Botón de “Añadir al carrito” conectado a la lógica del backend.

Plantillas reutilizables mediante herencia (base.html).

Esto permite separar claramente la lógica de presentación del resto de la aplicación.

### 4.5️ Administración de Django (Admin)

El panel de administración de Django ha sido configurado para facilitar la gestión del sistema:

Gestión completa de vendedores (Seller).

Alta, modificación y eliminación de clientes (Customer).

Gestión de productos (Product) con generación automática de slug.

Administración de pedidos (Order) con:

Filtro por estado y fecha.

Visualización de los productos incluidos en cada pedido mediante inlines.

Esto permite a los responsables del sistema realizar operaciones CRUD de forma sencilla sin necesidad de acceder al código.

---

## 5. Desarrollo Técnico de Funcionalidades

### 5.1 Gestión Dinámica del Carrito de Compras

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

### 5.2 Chatbot de Asistencia “Maranata”

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

### 5.3 Efecto Visual: Lluvia de Cruces

Para reforzar la identidad visual del sitio, se implementa un efecto animado en la vista de listado de productos.

Generación dinámica de elementos DOM mediante setInterval().

Parámetros aleatorios para posición horizontal y velocidad de caída.

Animaciones CSS3 usando @keyframes para traslación vertical y rotación.

Este efecto aporta dinamismo sin afectar significativamente al rendimiento.

### 5.4 Gestión de Formularios y Contacto

El sistema diferencia claramente entre formularios de negocio y formularios informativos:

CheckoutForm (ModelForm)
Vinculado directamente al modelo Order, permitiendo crear pedidos con form.save().

ContactForm (Form)
Formulario independiente con widgets de Bootstrap.
En la vista de contacto se muestra un aviso recomendando el uso previo del chatbot, reduciendo la carga de consultas manuales.

---

# 6. Diseño Responsive y Estilos

La interfaz utiliza Bootstrap 5.3 como base visual.

| Elemento             | Implementación                                               |
| -------------------- | ------------------------------------------------------------ |
| Hero sections        | Imágenes de fondo con overlays semitransparentes             |
| Tarjetas de producto | Sombras dinámicas y efecto `scale` al pasar el cursor        |
| Tablas de pedidos    | Clases `table-hover` y `align-middle` para mayor legibilidad |

---

# 7. Tecnologías Utilizadas

Python 3

Django

HTML5 / CSS3

JavaScript

Bootstrap 5.3

SQLite (entorno de desarrollo)

---

# 8. Conclusión

El proyecto Artesanía Cristiana combina una arquitectura web sólida con una identidad visual cuidada y una clara orientación social. La aplicación demuestra el uso práctico del framework Django para el desarrollo de plataformas web completas, integrando funcionalidades dinámicas, diseño responsive y una experiencia de usuario coherente.
