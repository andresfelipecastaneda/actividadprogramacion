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

    # Este es un nuevo metodo que permite modificar el cambio de cargo del usuario administrativo de forma controlada donde se valida que el nuevo cargo no sea vacio
    def cambiar_cargo(self, nuevo_cargo):
        """Permite cambiar el cargo del administrativo"""
        if nuevo_cargo != "":
            self.cargo = nuevo_cargo
        else:
            raise ValueError("El cargo no puede ser vacío")
        
    # Este es un metodo que permite actualizar los años de experiencia del usuario administrativo donde este valida que la experiencia sea un numero positivo
    def actualizar_experiencia(self, nueva_experiencia):
        """Permite actualizar los años de experiencia"""
        if nueva_experiencia >= 0:
            self.experiencia = nueva_experiencia
        else:
            raise ValueError("La experiencia debe ser un número positivo")
