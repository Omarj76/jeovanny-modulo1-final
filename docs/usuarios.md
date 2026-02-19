# Gestión de Biblioteca - Historias de Usuario

## 1. Registro de Nuevas Adquisiciones
**Actor:** Bibliotecario

**Descripción:** Registrar nuevos ejemplares en el sistema con título, autor e ID único.

**Objetivo:** Mantener el catálogo actualizado y disponible.

**Criterios de Aceptación:**
- El sistema rechaza registros con campos obligatorios faltantes
- El estado se asigna automáticamente como "Disponible"

---

## 2. Gestión de Préstamos Rápidos
**Actor:** Bibliotecario

**Descripción:** Asignar un libro a un usuario específico indicando su nombre.

**Objetivo:** Registrar quién tiene cada ejemplar y evitar pérdidas.

**Criterios de Aceptación:**
- El estado del libro cambia a "Prestado"
- Se genera automáticamente fecha de devolución a 14 días

---

## 3. Consulta de Disponibilidad
**Actor:** Usuario de la biblioteca

**Descripción:** Buscar un libro por título o ID.

**Objetivo:** Verificar disponibilidad antes de acudir al mostrador.

**Criterios de Aceptación:**
- La búsqueda muestra el estado actual (Disponible/Prestado) de forma clara

---

## 4. Control de Devoluciones
**Actor:** Bibliotecario

**Descripción:** Marcar un libro como devuelto mediante su ID.

**Objetivo:** Actualizar inmediatamente la disponibilidad en el catálogo.

**Criterios de Aceptación:**
- Se cierra el registro del préstamo actual
- El libro puede prestarse nuevamente de inmediato

---

## 5. Alerta de Plazos de Entrega
**Actor:** Administrador del sistema

**Descripción:** Resaltar préstamos que han superado la fecha límite.

**Objetivo:** Contactar usuarios morosos y recuperar el inventario.

**Criterios de Aceptación:**
- Existe una función/vista que filtra préstamos con fecha_entrega anterior a la actual
