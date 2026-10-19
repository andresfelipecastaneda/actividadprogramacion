# Se crea la clase que representa a las personas de la universidad

class Persona:
    # Este es el constructor que inicializa los atributos de la persona
    def __init__(self, identificacion, nombre, correo, telefono, direccion):
        # Aqui se usan los setters para validar los datos antes de asignarlos
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)
        self.set_direccion(direccion)

     # Metodos para consultar cada uno de los atributos de Persona
    def get_identificacion(self): return self._identificacion
    def get_nombre(self): return self._nombre
    def get_correo(self): return self._correo
    def get_telefono(self): return self._telefono
    def get_direccion(self): return self._direccion

    # Valida que la identificacion no sea un dato vacio
    def set_identificacion(self, identificacion):
        if identificacion != "":
            self._identificacion = identificacion
        else:
            raise ValueError("La identificación no puede ser vacía")

    # Valida que el nombre no sea un dato vacio
    def set_nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede ser vacío")

    # Valida que el correo no sea un dato vacio
    def set_correo(self, correo):
        if correo != "":
            self._correo = correo
        else:
            raise ValueError("El correo no puede ser vacío")

     # Valida que el correo no sea un dato vacio
    def set_telefono(self, telefono):
        if telefono != "":
            self._telefono = telefono
        else:
            raise ValueError("El teléfono no puede ser vacío")

    # Valida que  el correo no sea un dato vacio
    def set_direccion(self, direccion):
        if direccion != "":
            self._direccion = direccion
        else:
            raise ValueError("La dirección no puede ser vacía")

    # Este es el metodo que muestra la informacion de Persona
    def mostrar_informacion(self):
        return f"Identificación: {self._identificacion}, Nombre: {self._nombre}, Correo: {self._correo}, Teléfono: {self._telefono}, Dirección: {self._direccion}"
