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
