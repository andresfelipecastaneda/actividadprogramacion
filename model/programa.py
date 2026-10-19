# Se crea la clase que representan los programas academicos
class ProgramaAcademico:

    # Este es el constructor que inicializa los atributos
    def __init__(self, codigo, nombre, facultad, num_semestres, modalidad):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_facultad(facultad)
        self.set_num_semestres(num_semestres)
        self.set_modalidad(modalidad) 

    # Estos son los metodos que sirven para modificar los atributos con validaciones
    def get_codigo(self): return self._codigo
    def get_nombre(self): return self._nombre
    def get_facultad(self): return self._facultad
    def get_num_semestres(self): return self._num_semestres
    def get_modalidad(self): return self._modalidad

# Valida que el codigo no sea un dato vacio
    def set_codigo(self, codigo):
        if codigo != "":
            self._codigo = codigo
        else:
            raise ValueError("El código no puede ser vacío")

# Valida que el nombre no sea un dato vacio
    def set_nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede ser vacío")

# Valida que la facultad no sea un dato vacio
    def set_facultad(self, facultad):
        if facultad != "":
            self._facultad = facultad
        else:
            raise ValueError("La facultad no puede ser vacía")

# Valida que el numero de semestres sea mayor que 0
    def set_num_semestres(self, num_semestres):
        if num_semestres > 0:
            self._num_semestres = num_semestres
        else:
            raise ValueError("El número de semestres debe ser mayor que 0")

# Valida que la modalidad no sea un dato diferente a Presencial, virtual o mixta
    def set_modalidad(self, modalidad):
        if modalidad in ["Presencial", "Virtual", "Mixta"]:
            self._modalidad = modalidad
        else:
            raise ValueError("La modalidad debe ser Presencial, Virtual o Mixta")

# Este es el metodo que muestra la informacion del programa
    def mostrar_informacion(self):
        return f"Programa {self._codigo}: {self._nombre}, Facultad: {self._facultad}, Semestres: {self._num_semestres}, Modalidad: {self._modalidad}"
