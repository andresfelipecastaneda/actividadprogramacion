 # Se crea la clase que representa a los docentes de la universidad
from model.persona import Persona

class Docente(Persona):
    def __init__(self, identificacion, nombre, correo, telefono, direccion, num_empleado, facultad, tipo_contratacion, horas, especialidad):
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
