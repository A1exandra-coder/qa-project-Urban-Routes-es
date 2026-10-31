# Proyecto Sprint 9: Pruebas automatizadas de Urban Routes

## 1. Descripción del proyecto

Este proyecto consiste en automatizar el proceso de solicitud de un taxi en la aplicación Urban Routes mediante pruebas automatizadas con Python y Selenium.

El objetivo es comprobar diferentes funcionalidades del proceso de solicitud de un viaje, desde la configuración de la ruta hasta la selección de servicios adicionales.

## 2. Tecnologías y herramientas utilizadas

- Python 3.14.7
- Selenium WebDriver
- Pytest
- PyCharm
- Google Chrome
- Git y GitHub

## 3. Estructura del proyecto

- `main.py`: contiene los localizadores, métodos de interacción con la aplicación y la prueba automatizada.
- `data.py`: contiene los datos de prueba, como las direcciones, el número telefónico, los datos de tarjeta y el mensaje para el conductor.
- `README.md`: contiene la descripción del proyecto, las herramientas utilizadas y las instrucciones de ejecución.

## 4. Funcionalidades trabajadas

Se implementaron métodos para automatizar las siguientes acciones:

1. Configurar las direcciones de origen y destino.
2. Seleccionar el servicio de taxi.
3. Elegir la tarifa Comfort.
4. Abrir el formulario de teléfono e introducir el número.
5. Solicitar y recuperar el código de confirmación mediante la función proporcionada `retrieve_phone_code()`.
6. Seleccionar el método de pago e introducir los datos de la tarjeta.
7. Introducir un mensaje para el conductor.
8. Solicitar manta y pañuelos.
9. Agregar dos helados.
10. Interactuar con el botón de solicitud del servicio.

## 5. Datos de prueba

Los datos utilizados se encuentran centralizados en `data.py`, para facilitar su mantenimiento y reutilización.

Se utilizaron las direcciones de prueba proporcionadas para el ejercicio, junto con los datos de teléfono, tarjeta y mensaje para el conductor.

## 6. Ejecución de las pruebas

Para ejecutar la prueba automatizada:

1. Abrir el proyecto en PyCharm.
2. Activar el entorno virtual.
3. Abrir la terminal del proyecto.
4. Ejecutar el siguiente comando:

```bash
python -m pytest main.py -v -s --tb=short
```

Para comprobar la sintaxis de los archivos:

```bash
python -m py_compile main.py
python -m py_compile data.py
```

## 7. Resultados y observaciones

Durante el desarrollo se ejecutaron pruebas sucesivas para identificar y corregir inconvenientes en la interacción con los elementos de la aplicación.

Se presentaron dificultades relacionadas con:

- La recuperación del código de confirmación telefónica mediante `retrieve_phone_code()`.
- La validación del número telefónico en la aplicación, que mostró el mensaje «Introduce el número correcto».
- La interacción con algunos elementos de la interfaz que inicialmente no estaban disponibles para recibir clics.
- La superposición de elementos de la interfaz sobre el botón de solicitud.

Se realizaron ajustes en la interacción con los elementos de la página y se verificó nuevamente la ejecución.

**Resultado de la última ejecución registrada:** `1 passed`.

**Limitación pendiente:** aunque la última ejecución terminó correctamente, durante las pruebas manuales se observó que la aplicación rechazaba el número telefónico utilizado. Por esta razón, la validación telefónica y la recuperación del código deben considerarse un punto pendiente de verificación. No se afirma que el flujo completo de confirmación telefónica haya quedado validado.

La función `retrieve_phone_code()` proporcionada en el proyecto se conservó sin modificaciones.

## 8. Control de versiones

El proyecto fue publicado en GitHub y se realizó un commit con el mensaje:

`Entrega Sprint 9 - automatizacion Urban Routes`

Los archivos `README.md`, `data.py` y `main.py` fueron enviados correctamente a la rama `main`.

Repositorio:

https://github.com/A1exandra-coder/qa-project-Urban-Routes-es

## 9. Conclusión

Se desarrollaron métodos de automatización para las principales etapas del proceso de solicitud de un taxi en Urban Routes, utilizando Python, Selenium y Pytest.

Se documentaron los inconvenientes encontrados, las correcciones realizadas y los puntos que requieren verificación adicional, manteniendo un registro transparente del proceso de pruebas.