# Script de Automatización con Pyhton de Consolidación y Envío de Reportes de Programación en Excel

## Descripción General
Este proyecto consiste en un script desarrollado en Python que automatiza el proceso de consolidación de archivos Excel de programación y el envío masivo de correos electrónicos con el reporte consolidado. La herramienta permite leer múltiples archivos conun mismo formato, consolidarlos en un único archivo, personalizar las plantillas de correo según el tipo de destinatario y enviar los reportes de forma automatizada, generando además un registro de auditoría detallado de cada acción.

**Las 4 tareas principales del sistema:**
- Leer y procesar múltiples archivos Excel
- Consolidar automáticamente los datos en un único archivo
- Personalizar el correo según el tipo de destinatario (programación o guardia)
- Enviar correos con el archivo adjunto y registrar cada acción

**Capacidad del sistema:**
- Manejo de archivos Excel con estructuras variables (detección automática de formato)
- Generación de versiones consecutivas diferenciados por numero de version
- Envío por grupos según tipo de destinatario
- Envio en cuentas personales (Gmail, Hotmail) cuenta con una capacidad de hasta 500 envíos diarios
- Envio en cuentas corporativas cuenta con una capacidad hasta 2000 envíos diarios

## Tipos de Correos Generados
El sistema utiliza plantillas personalizadas según el tipo de destinatario, que se definen en el archivo de destinatarios.

- Correo tipo Programación: Diseñado para el personal administrativo y de programación. Incluye el reporte consolidado completo de todas las sedes con la información detallada de programación.
![](iconos/correoprogramacion.png)

- Correo tipo Guardia: Orientado al personal de seguridad y guardia. Incluye el reporte específico de programación para el personal de guardia.
![](iconos/correoguardia.png)
Ambas plantillas son completamente personalizables desde el archivo plantillas_correo.py, donde se puede modificar el texto, asunto y estructura según los requerimientos, en este caso se aplicaron formatos basicos.



<table>
  <thead>
    <tr>
      <th>Módulo / Archivo</th>
      <th>Responsabilidad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>main.py</code></td>
      <td>Orquestador principal: coordina consolidación, carga destinatarios y envía correos</td>
    </tr>
    <tr>
      <td><code>consolidacion.py</code></td>
      <td>Detecta estructura de archivos Excel, consolida datos y genera versiones numeradas</td>
    </tr>
    <tr>
      <td><code>enviar_email.py</code></td>
      <td>Construye mensaje con adjunto MIME y envía vía SMTP (Gmail)</td>
    </tr>
    <tr>
      <td><code>config/credentials.py</code></td>
      <td>Almacena credenciales SMTP para autenticación</td>
    </tr>
    <tr>
      <td><code>config/plantillas_correo.py</code></td>
      <td>Define plantillas de asunto y cuerpo según tipo de destinatario</td>
    </tr>
    <tr>
      <td><code>config/destinatarios.xlsx</code></td>
      <td>Lista de correos electrónicos agrupados por tipo (programación/guardia)</td>
    </tr>
    <tr>
      <td><code>datasets/</code></td>
      <td>Contiene archivos fuente (ProgramacionSede*.xlsx) y consolidados generados (ProgramacionGeneral_*.xlsx)</td>
    </tr>
  </tbody>
</table>
