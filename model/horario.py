# Se crea la clase que representa el horario de un grupo académico
class Horario:
    # Constructor que inicializa los atributos del horario
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.set_dia(dia)
        self.set_hora_inicio(hora_inicio)
        self.set_hora_fin(hora_fin)
        self.set_salon(salon)

    # Métodos GET
    def get_dia(self): return self._dia
    def get_hora_inicio(self): return self._hora_inicio
    def get_hora_fin(self): return self._hora_fin
    def get_salon(self): return self._salon

    # Métodos SET con validaciones
    def set_dia(self, dia):
        if dia != "":
            self._dia = dia
        else:
            raise ValueError("El día no puede ser vacío")

    def set_hora_inicio(self, hora_inicio):
        if hora_inicio != "":
            self._hora_inicio = hora_inicio
        else:
            raise ValueError("La hora de inicio no puede ser vacía")

    def set_hora_fin(self, hora_fin):
        if hora_fin != "":
            self._hora_fin = hora_fin
        else:
            raise ValueError("La hora de finalización no puede ser vacía")

    def set_salon(self, salon):
        if salon != "":
            self._salon = salon
        else:
            raise ValueError("El salón no puede ser vacío")

    # Método para mostrar la información del horario
    def mostrar_informacion(self):
        return (f"{self._dia} | {self._hora_inicio} - {self._hora_fin} | Salón: {self._salon}")

    # ---------------- NUEVA PARTE ----------------
    # Métodos adicionales para segunda versión
    def cambiar_salon(self, nuevo_salon):
        """Permite cambiar el salón del horario"""
        if nuevo_salon != "":
            self._salon = nuevo_salon
        else:
            raise ValueError("El salón no puede ser vacío")

    def actualizar_horas(self, nueva_hora_inicio, nueva_hora_fin):
        """Permite actualizar las horas del horario"""
        if nueva_hora_inicio != "" and nueva_hora_fin != "":
            self._hora_inicio = nueva_hora_inicio
            self._hora_fin = nueva_hora_fin
        else:
            raise ValueError("Las horas no pueden ser vacías")
