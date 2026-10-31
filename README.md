# Proyecto Sprint 9: Pruebas automatizadas de Urban Routes

## Descripción del proyecto
Este proyecto consiste en automatizar el proceso de solicitud de un taxi en la aplicación Urban Routes, utilizando Selenium y Python.

## Tecnologías utilizadas
- Python
- Selenium WebDriver
- Pytest
- Google Chrome
- PyCharm

## Pruebas automatizadas
El flujo automatizado contempla las siguientes acciones:

1. Configurar la dirección de origen y destino.
2. Seleccionar la tarifa Comfort.
3. Introducir y confirmar el número de teléfono.
4. Agregar una tarjeta bancaria.
5. Escribir un mensaje para el conductor.
6. Solicitar manta y pañuelos.
7. Agregar dos helados.
8. Confirmar la solicitud del viaje.

## Estructura del proyecto
- `main.py`: contiene los localizadores, métodos y pruebas automatizadas.
- `data.py`: contiene los datos utilizados durante las pruebas.
- `README.md`: documentación del proyecto.

## Cómo ejecutar las pruebas

1. Abrir el proyecto en PyCharm.
2. Activar el entorno virtual.
3. Abrir la terminal del proyecto.
4. Ejecutar el siguiente comando:

```bash
python -m pytest main.py -v -s --tb=short
```

## Resultado de las pruebas
La prueba automatizada `test_set_route` se ejecutó correctamente:

**Resultado: 1 passed.**

