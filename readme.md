# Sistema de Gestión de Mensajes

Este sistema facilita la comunicación entre productores y consumidores mediante un broker centralizado.

## Descripción

El Sistema de Gestión de Mensajes permite a los productores enviar mensajes al broker, que a su vez los encola y los distribuye a los consumidores interesados. Los mensajes están estructurados en formato JSON y pueden contener información como timestamp, identificación única, encabezado y cuerpo del mensaje.

## Instrucciones

Sigue estos pasos para configurar y utilizar el sistema:

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local utilizando el siguiente comando:

2. **Configurar el Entorno**:
- Asegúrate de tener Python 3 instalado en tu sistema.
- Instala las dependencias necesarias

3. **Ejecutar el main**:
- Ejecuta el main en una terminal utilizando el siguiente comando:

  ```
  python main.py
  ```

5. **Observar la Comunicación**:
- Observa cómo los mensajes son enviados desde los productores al broker y luego distribuidos a los consumidores.

## Requisitos del Sistema

- Python 3.x
- Bibliotecas adicionales: `avro-python3`, `socket`




