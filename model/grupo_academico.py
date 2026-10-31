# Se crea la clase que representa los grupos académicos de la universidad
from model.excepciones import (
    EstudianteYaMatriculadoError,
    GrupoLlenoError,
    EstudianteNoEncontradoError
)

class GrupoAcademico:
    # Constructor que inicializa los atributos del grupo académico
    def __init__(self, codigo_grupo, asignatura, docente, capacidad_maxima, horario):
        self.codigo_grupo = codigo_grupo
        self.asignatura = asignatura   # objeto Asignatura
        self.docente = docente         # objeto Docente
        self.capacidad_maxima = capacidad_maxima
        self.horario = horario         # objeto Horario (composición)
        self.estudiantes = []          # lista de objetos Estudiante

    # Método que muestra la información del grupo
    def mostrar_informacion_grupo(self):
        return (f"Grupo {self.codigo_grupo} | Asignatura: {self.asignatura.get_nombre()} "
                f"| Docente: {self.docente.get_nombre()} | Capacidad: {self.capacidad_maxima} "
                f"| Horario: {self.horario.mostrar_informacion()}")

    # Método para matricular estudiante
    def matricular_estudiante(self, estudiante):
        # Validar si ya está matriculado
        for est in self.estudiantes:
            if est.codigo_est == estudiante.codigo_est:
                raise EstudianteYaMatriculadoError(
                    f"El estudiante {estudiante.get_nombre()} ya está matriculado en el grupo {self.codigo_grupo}"
                )
        # Validar capacidad
        if len(self.estudiantes) >= self.capacidad_maxima:
            raise GrupoLlenoError(
                f"El grupo {self.codigo_grupo} ya alcanzó su capacidad máxima"
            )
        # Agregar estudiante
        self.estudiantes.append(estudiante)

    # Método para retirar estudiante
    def retirar_estudiante(self, codigo_estudiantil):
        for est in self.estudiantes:
            if est.codigo_est == codigo_estudiantil:
                self.estudiantes.remove(est)
                return
        # Si no se encuentra
        raise EstudianteNoEncontradoError(
            f"El estudiante con código {codigo_estudiantil} no está matriculado en el grupo {self.codigo_grupo}"
        )

    # Método para mostrar lista de estudiantes
    def mostrar_estudiantes(self):
        if not self.estudiantes:
            return f"No hay estudiantes matriculados en el grupo {self.codigo_grupo}"
        return "\n".join([est.mostrar_informacion() for est in self.estudiantes])

    # ---------------- NUEVA PARTE ----------------
    # Métodos adicionales para segunda versión
    def contar_estudiantes(self):
        """Devuelve el número actual de estudiantes matriculados"""
        return len(self.estudiantes)

    def verificar_disponibilidad(self):
        """Indica si aún hay cupos disponibles en el grupo"""
        return self.capacidad_maxima - len(self.estudiantes)
