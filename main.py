# Aqui se importan las clases que se van a usar
from model.programa import ProgramaAcademico
from model.asignatura import Asignatura
from model.estudiante import Estudiante
from model.docente import Docente
from model.administrativo import Administrativo

# Creación de programas académicos que se dictan en la universidad

programa1 = ProgramaAcademico("INF01", "Ingeniería de Sistemas", "Facultad de Ingeniería", 10, "Presencial")
programa2 = ProgramaAcademico("ADM01", "Administración de Empresas", "Facultad de Ciencias Económicas", 8, "Virtual")

# Creación de asignaturas de cada programa

asignatura1 = Asignatura("INF101", "Programación I", 4, programa1, 1, "Obligatoria")
asignatura2 = Asignatura("ADM201", "Contabilidad Básica", 3, programa2, 2, "Obligatoria")


# Creación de estudiantes de cada programa

estudiante1 = Estudiante("1105464590", "Andres Felipe Castañeda", "acastaneda@umanizales.edu.co", "3107951262", "Calle 80 No 7 - 25 Ibagué", "EST00001", programa1, 2, 4.2, "Activo")
estudiante2 = Estudiante("1110838938", "Pepito Perez", "pepitoperez@umanizales.edu.co", "3119876543", "Carrera 15 No 8-30 Manizales", "EST00002", programa2, 4, 3.8, "Activo")


# Creación de docentes que dictan clase

docente1 = Docente("1110748390", "Luis Rodriguez", "luisrodriguez@umanizales.edu.co", "3124567890", "Avenida 3 No 45-67 Manizales", "DOC00001", "Ingeniería", "Tiempo completo", 40, "Programación")
docente2 = Docente("1000394938", "Natalia Castellanos", "nataliacastellanos@correo.com", "3136549870", "Calle 20 No 10-15 Manizales", "DOC00002", "Ciencias Económicas", "Medio tiempo", 20, "Contabilidad")


# Creación de administrativos que laboran en la universidad

administrativo1 = Administrativo("3001", "Pedro Lopez", "pedrolopez@umanizales.edu.co", "3147896540", "Carrera 7 No 12-34 Manizales", "ADM01", "Registro Académico", "Jefe de área", "Diurna", 15)
administrativo2 = Administrativo("3002", "Diana Cabezas", "dianacabezas@umanizales.edu.co", "3159873210", "Calle 25 No 9-40 Manizales", "ADM02", "Bienestar Universitario", "Coordinadora", "Nocturna", 8)


# Aca se muestran los diferentes tipos de personas en una misma lista

personas = [estudiante1, estudiante2, docente1, docente2, administrativo1, administrativo2]


# Cada objeto ejecuta sus propios métodos donde uno muestra los datos completos y el otro muestra la actividad principal

for persona in personas:
    print(persona.mostrar_informacion())          
    print(persona.realizar_actividad_principal()) 
    print("--------------------------------------------------")


# Se cambia el nombre de un estudiante 
estudiante1.set_nombre("Andres F. Castañeda")
print("Después de modificar el nombre del estudiante:")
print(estudiante1.mostrar_informacion())
print("--------------------------------------------------")

# Aca muestra si la modalidad es invalida
try:
    programa1.set_modalidad("Híbrida")
except ValueError as e:
    print("Dato inválido:", e)

# Muestra si el nombre es un dato vacio
try:
    estudiante2.set_nombre("")  
except ValueError as e:
    print("Dato inválido:", e)

# Muestra si el numero de semestres es invalido
try:
    programa2.set_num_semestres(0)  
except ValueError as e:
    print("Dato inválido:", e)
