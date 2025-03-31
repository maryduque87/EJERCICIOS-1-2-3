class Estudiante ():
  Nombre: "Maria"
  Apellido: "Duque"
  Calificacion: "4.5"

estudiante1 = Estudiante ()
estudiante2 = Estudiante ()
estudiante3 = Estudiante ()

class Estudiante ():
  def __init__(self, nombre, apellido, calificacion):
    self.nombre = nombre
    self.apellido = apellido
    self.calificacion = float(calificacion)

estudiante1 = Estudiante ("Maria", "Duque", "4.5")
estudiante2 = Estudiante ("Camilo", "Mejia", "5.0")
estudiante3 = Estudiante ("Loraine", "Acosta", "2.9")

print(f"Nombre: {estudiante1.nombre}")
print(f"Apellido: {estudiante1.apellido}")
print(f"Calificacion: {estudiante1.calificacion}")

estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in estudiantes:
    print(f"Nombre: {estudiante.nombre}")
    print(f"Apellido: {estudiante.apellido}")
    print(f"Calificación: {estudiante.calificacion}")

    if estudiante.calificacion >= 3.0:
        print("Aprobado")
    else:
        print("Reprobado")
    print("-----------")
