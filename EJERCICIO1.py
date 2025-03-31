class GestionDeUnaBiblioteca:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        """Muestra la información del libro."""
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        """Actualiza el número de páginas del libro."""
        if nuevas_paginas > 0:
            self.num_paginas = nuevas_paginas
            print("Número de páginas actualizado correctamente.")
        else:
            print("El número de páginas debe ser mayor que 0.")

# aqui creo un objeto con el nombre del libro
libro1 = GestionDeUnaBiblioteca("Culpa Tuya", "Mercedes Ron", 448)
libro1.mostrar_informacion()

# realizo lo siguiente para actualizar el numero de la paguina
libro1.actualizar_paginas(460)
libro1.mostrar_informacion()

