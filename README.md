Nombre: Andres Felipe Castañeda Montesinos

Este proyecto consiste en el desarrollo de un sistema de gestion academico en Python orientado a objetos, que permite gestionar programas academicos, asignaturas
y personas relacionadas con la universidad, como lo que son estudiantes, docentes y administrativos.
Se implementan clases con atributos encapsulados, validaciones mediante setters y métodos para mostrar información y realizar actividades principales. El programa 
principal (main.py) demuestra las pruebas mínimas de funcionamiento como creación de programas y asignaturas, creación de al menos seis personas, consulta de 
información, modificación de datos válidos, manejo de valores inválidos, presentación particular de cada tipo de persona y recorrido polimórfico de la colección 
de personas.

A continuacion esta es la estructura de los archivos:
actividadprogramacion/model/ administrativo.py - asignatura.py - docente.py - estudiante.py - persona.py - programa.py
actividadprogramacion/main.py

Para ejecutar el programa se debe copiar el enlace de GitHub "https://github.com/andresfelipecastaneda/actividadprogramacion.git", pegar en el navegador y descargarlo, luego abrir la carpeta del proyecto. Despues ejecutar el programa en la terminal "py main.py" y por
ultimo revisar la salida de la consola donde se van a mostrar toda la información.

En este proyecto se aplican tres conceptos básicos de la programación orientada a objetos como la herencia, sobreescritura y polimorfismo. La herencia se usa porque 
la clase Persona es la base y de ella se derivan Estudiante, Docente y Administrativo, que comparten atributos comunes pero también tienen características propias.
La sobreescritura aparece cuando estas clases hijas redefinen métodos como mostrar_informacion y realizar_actividad_principal, adaptándolos a lo que cada tipo de 
persona necesita mostrar. Finalmente, el polimorfismo se ve cuando se recorre una lista con diferentes tipos de personas y se llaman los mismos métodos; aunque el 
nombre del método es igual, cada objeto responde de manera distinta según su clase, mostrando comportamientos diferentes bajo una misma instrucción.
