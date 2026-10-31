# Cuando un estudiante ya está matriculado en el grupo
class EstudianteYaMatriculadoError(Exception):
    def __init__(self, mensaje="El estudiante ya está matriculado en el grupo"):
        super().__init__(mensaje)

# Cuando el grupo alcanza su capacidad máxima
class GrupoLlenoError(Exception):
    def __init__(self, mensaje="El grupo alcanzó su capacidad máxima"):
        super().__init__(mensaje)

# Cuando se intenta retirar un estudiante que no está matriculado
class EstudianteNoEncontradoError(Exception):
    def __init__(self, mensaje="El estudiante no está matriculado en el grupo"):
        super().__init__(mensaje)

# Cuando la asignatura buscada no existe
class AsignaturaNoExisteError(Exception):
    def __init__(self, mensaje="La asignatura buscada no existe"):
        super().__init__(mensaje)

# Cuando el programa académico buscado no existe
class ProgramaNoExisteError(Exception):
    def __init__(self, mensaje="El programa académico buscado no existe"):
        super().__init__(mensaje)

# ---------------- NUEVA PARTE ----------------
# Excepciones adicionales para segunda versión
# Cuando el horario asignado es inválido
class HorarioInvalidoError(Exception):
    def __init__(self, mensaje="El horario asignado no es válido"):
        super().__init__(mensaje)

# Cuando se intenta asignar un docente que no pertenece a la facultad correspondiente
class DocenteNoPerteneceError(Exception):
    def __init__(self, mensaje="El docente no pertenece a la facultad de la asignatura"):
        super().__init__(mensaje)
