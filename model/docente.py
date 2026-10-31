# Se crea la clase que representa a los docentes de la universidad
from model.persona import Persona

class Docente(Persona):
    def __init__(self, identificacion, nombre, correo, telefono, direccion,
                 num_empleado, facultad, tipo_contratacion, horas, especialidad):
        super().__init__(identificacion, nombre, correo, telefono, direccion)
        self.num_empleado = num_empleado
        self.facultad = facultad
        self.tipo_contratacion = tipo_contratacion
        self.horas = horas
        self.especialidad = especialidad

    # El metodo que muestra la informacion del docente
    def mostrar_informacion(self):
        return (f"{super().mostrar_informacion()} | Empleado: {self.num_empleado}, "
                f"Facultad: {self.facultad}, Contrato: {self.tipo_contratacion}, "
                f"Horas: {self.horas}, Especialidad: {self.especialidad}")
    
    # El metodo que describe la actividad principal del docente
    def realizar_actividad_principal(self):
        return f"El docente orienta clases en la facultad {self.facultad}, área de {self.especialidad}"

    # Este metodo permite cambiar el tipo de contratacion del docente donde se valida que el nuevo tipo de contratacion este dentro de las opciones permitidas, si es tiempo completo - medio tiempo o catedra
    def cambiar_tipo_contratacion(self, nuevo_tipo):
        """Permite cambiar el tipo de contratación del docente"""
        if nuevo_tipo in ["Tiempo completo", "Medio tiempo", "Cátedra"]:
            self.tipo_contratacion = nuevo_tipo
        else:
            raise ValueError("El tipo de contratación debe ser Tiempo completo, Medio tiempo o Cátedra")

    # Este metodo permite actualizar las horas de trabajo del docente donde valida que las horas deban ser mayores a 0
    def actualizar_horas(self, nuevas_horas):
        """Permite actualizar las horas de trabajo del docente"""
        if nuevas_horas > 0:
            self.horas = nuevas_horas
        else:
            raise ValueError("Las horas deben ser mayores que 0")
