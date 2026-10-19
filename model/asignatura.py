# Se crea la clase que representa las asignaturas de los programas académicos
class Asignatura:
    # Este es el constructor que inicializa los atributos de la asignatura
    def __init__(self, codigo, nombre, num_creditos, programa, semestre_oferta, tipo_asignatura):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        self.set_num_creditos(num_creditos)
        self.set_programa(programa)
        self.set_semestre_oferta(semestre_oferta) 
        self.set_tipo_asignatura(tipo_asignatura)  

    # Este es el metodo que muestra toda la información de la asignatura
    def get_codigo(self): return self._codigo
    def get_nombre(self): return self._nombre
    def get_num_creditos(self): return self._num_creditos
    def get_programa(self): return self._programa
    def get_semestre_oferta(self): return self._semestre_oferta
    def get_tipo_asignatura(self): return self._tipo_asignatura

   # Valida que el codigo no sea un dato nulo
    def set_codigo(self, codigo):
        if codigo != "":
            self._codigo = codigo
        else:
            raise ValueError("El código no puede ser vacío")

   # Valida que el nombre no sea un dato nulo
    def set_nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede ser vacío")

   # Valida que el numero de creditos sea mayor que 0 
    def set_num_creditos(self, num_creditos):
        if num_creditos > 0:
            self._num_creditos = num_creditos
        else:
            raise ValueError("El número de créditos debe ser mayor que 0")

# Valida que el codigo no sea un dato nulo
    def set_programa(self, programa):
        if programa is not None:
            self._programa = programa
        else:
            raise ValueError("La asignatura debe pertenecer a un programa")

# Valida que el semestre de oferta deba ser mayor que 0
    def set_semestre_oferta(self, semestre_oferta):
        if semestre_oferta > 0:
            self._semestre_oferta = semestre_oferta
        else:
            raise ValueError("El semestre de oferta debe ser mayor que 0")

# Valida que el tipo de asignatura sea obligatoria o electiva
    def set_tipo_asignatura(self, tipo_asignatura):
        if tipo_asignatura in ["Obligatoria", "Electiva"]:
            self._tipo_asignatura = tipo_asignatura
        else:
            raise ValueError("El tipo de asignatura debe ser Obligatoria o Electiva")

# Este es el metodo que muestra toda la información de la asignatura
    def mostrar_informacion(self):
        return (f"Asignatura {self._codigo}: {self._nombre}, Créditos: {self._num_creditos}, "
                f"Programa: {self._programa.get_nombre()}, Semestre de oferta: {self._semestre_oferta}, "
                f"Tipo: {self._tipo_asignatura}")
