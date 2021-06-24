class Animal:

    def __init__(self, nombre: str, edad, salud: int, felicidad: int):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
        self.especies = str()

    def display_info(self):
        info = f"Esta especie es: {self.especies}, se llama: {self.nombre}, y su salud es de: {self.salud} y su felicidad es de: {self.felicidad}"
        return info

    def alimentacion(self):
        self.salud += 10
        self.felicidad += 10

class Tigre(Animal):
    def __init__(self, nombre: str, edad = "desconocida", salud: int = 3, felicidad: int = 5, masculino: bool = True):
        super().__init__(nombre, edad, salud, felicidad)
        self.masculino = masculino


