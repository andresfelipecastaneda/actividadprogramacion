# Se crea la clase que representa a los estudiantes de la universidad
from model.persona import Persona

class Estudiante(Persona):

    # Este es el constructor que inicializa los atributos del estudiante
    def __init__(self, identificacion, nombre, correo, telefono, direccion, codigo_est, programa, semestre, promedio, estado):
        super().__init__(identificacion, nombre, correo, telefono, direccion)
        self.codigo_est = codigo_est
        self.programa = programa
        self.semestre = semestre
        self.promedio = promedio
        self.estado = estado 

    # El metodo que muestra la informacion del estudiante
    def mostrar_informacion(self):
        return (f"{super().mostrar_informacion()} | Código: {self.codigo_est}, "
                f"Programa: {self.programa.get_nombre()}, Semestre: {self.semestre}, "
                f"Promedio: {self.promedio}, Estado: {self.estado}")
    
    # El metodo que describe la actividad principal del estudiante
    def realizar_actividad_principal(self):
        return f"El estudiante cursa {self.programa.get_nombre()} en el semestre {self.semestre}"

    # El metodo permite actualizar el promedio del estudiante, donde valida que el promedio debe estar entre 0 y 5
    def actualizar_promedio(self, nuevo_promedio):
        """Permite actualizar el promedio del estudiante con validación"""
        if nuevo_promedio >= 0 and nuevo_promedio <= 5:
            self.promedio = nuevo_promedio
        else:
            raise ValueError("El promedio debe estar entre 0 y 5")

    # El metodo permite cambiar el estado del estudiante, donde valida que este estado este dentro de las opciones, si el estudiante esta activo o inactivo
    def cambiar_estado(self, nuevo_estado):
        """Permite cambiar el estado del estudiante (Activo/Inactivo)"""
        if nuevo_estado in ["Activo", "Inactivo"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("El estado debe ser Activo o Inactivo")
