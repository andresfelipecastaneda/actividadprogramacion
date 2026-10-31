# Documento de Decisiones de Diseño – Sistema de Gestión Académica

## 1. Introducción
Este documento describe las principales decisiones de diseño tomadas en el desarrollo del sistema académico. Se incluyen las alternativas consideradas, las opciones elegidas y la justificación de cada decisión, relacionándolas con los requerimientos de la actividad.

---

## 2. Tabla de Decisiones de Diseño

| Decisión de diseño | Alternativas descartadas | Opción elegida | Justificación detallada |
|---------------------|--------------------------|----------------|-------------------------|
| **Creación de clase base Persona** | Definir atributos separados en cada clase hija | Crear clase abstracta `Persona` con atributos comunes | Se descartó la alternativa porque generaría duplicación de código y dificultaría el mantenimiento. La clase abstracta permite reutilizar atributos comunes y obliga a las clases hijas a implementar su propia actividad principal. |
| **Clases hijas (Estudiante, Docente, Administrativo)** | Usar una sola clase genérica | Definir clases específicas que heredan de `Persona` | Se descartó la clase genérica porque no permitiría diferenciar atributos y comportamientos propios de cada rol. Con clases hijas se logra especialización: el estudiante tiene semestre y programa, el docente tiene tipo de contratación y horas, y el administrativo tiene cargo y experiencia. Cada uno implementa `realizar_actividad_principal()` de forma distinta. |
| **Programas y asignaturas** | Manejar asignaturas como texto plano | Crear clases `ProgramaAcademico` y `Asignatura` | Se descartó el manejo plano porque no permitiría validaciones ni relaciones complejas. Con clases se logra composición donde el programa mantiene una lista de asignaturas. Además, se implementó relación bidireccional: al asignar programa, la asignatura se agrega automáticamente al programa. |
| **Grupos académicos** | Relacionar estudiantes directamente con asignaturas | Crear clase `GrupoAcademico` con código, docente, horario y cupo | Se descartó la relación directa porque no refleja cómo funciona realmente la matrícula. Los estudiantes se inscriben en grupos, no en asignaturas sueltas. El grupo permite aplicar reglas: cupo máximo, matrícula duplicada, retiro de estudiantes. |
| **Horarios** | Representar horarios como cadenas de texto | Crear clase `Horario` con atributos y métodos | Se descartó el texto plano porque no permite validaciones ni flexibilidad. Con la clase `Horario` se asegura integridad: las horas deben ser válidas y el salón puede cambiarse sin romper el sistema. |
| **Manejo de errores** | Usar solo excepciones genéricas de Python | Definir excepciones personalizadas (`GrupoLlenoError`, `EstudianteYaMatriculadoError`, `EstudianteNoEncontradoError`, etc.) | Se descartó el uso exclusivo de excepciones genéricas porque no permiten identificar claramente el tipo de error. Con excepciones personalizadas se mejora la claridad y se manejan errores específicos de las reglas académicas. |
| **Validaciones de datos** | Permitir valores vacíos o inválidos | Implementar setters y validaciones en atributos | Se descartó permitir valores inválidos porque afectaría la integridad del sistema. Con validaciones se asegura consistencia: créditos > 0, tipo de asignatura válido, semestre de oferta mayor que 0. |

---

## 3. Conclusión
Las decisiones de diseño tomadas garantizan que el sistema sea robusto, extensible y fiel a la realidad académica. Se aplicaron principios de POO como herencia, polimorfismo, composición y manejo de excepciones personalizadas. Además, se añadieron validaciones para asegurar integridad de datos y métodos adicionales en la segunda versión para reflejar la evolución del sistema.
