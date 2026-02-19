
# Diagrama de Flujo: Proceso de Préstamo

## 🔍 Explicación de los Puntos de Decisión

### Validación de Existencia
El sistema primero verifica que el ID ingresado esté en la base de datos para evitar errores de referencia.

### Estado de Disponibilidad
Es el filtro de seguridad (que validamos en tu Test 2). Si el campo disponible es 0, el flujo se detiene para evitar que un libro tenga dos dueños a la vez.

### Automatización de Fechas
No permitimos que el bibliotecario elija la fecha manualmente; el sistema la impone según la política de la empresa (14 días) para evitar favoritismos o errores humanos.

### Persistencia Atómica
La actualización del libro y la creación del préstamo deben ocurrir juntas. Si una falla, la otra no debería ejecutarse (integridad de datos).
