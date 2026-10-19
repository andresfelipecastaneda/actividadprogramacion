# Se crea la clase que representa a los administrativos de la universidad
from model.persona import Persona

class Administrativo(Persona):

    # Constructor que inicializa los atributos del personal administrativo
    def __init__(self, identificacion, nombre, correo, telefono, direccion,
                 num_empleado, dependencia, cargo, jornada, experiencia):
        super().__init__(identificacion, nombre, correo, telefono, direccion)
        self.num_empleado = num_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada
        self.experiencia = experiencia 

# Este es el metodo para mostrar toda la informacion de cada uno de los administrativos de la universidad
    def mostrar_informacion(self):
        return (f"{super().mostrar_informacion()} | Empleado: {self.num_empleado}, "
                f"Dependencia: {self.dependencia}, Cargo: {self.cargo}, "
                f"Jornada: {self.jornada}, Experiencia: {self.experiencia} años")

# Este metodo describe la actividad principal del administrativo
    def realizar_actividad_principal(self):
        return f"El administrativo desempeña el cargo {self.cargo} en la dependencia {self.dependencia}"
