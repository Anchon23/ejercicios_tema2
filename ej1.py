import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def galaxia(self):
        if self.x < 0:
            return "Galaxia Via Lacta"
        elif self.x >= 0 and self.y < 0:
            return "Galaxia Andromeda"
        elif self.x >= 0 and self.y >= 0 and self.z < 0:
            return "Galaxia Pegaso"
        else:
            return "Galaxia Desconocida"

    def distancia(self, otra_estrella):
        dist_x = self.x - otra_estrella.x
        dist_y = self.y - otra_estrella.y
        dist_z = self.z - otra_estrella.z
        distancia = math.sqrt(dist_x**2 + dist_y**2 + dist_z**2)
        return distancia

# Ejemplo de uso
estrella_A = Estrella(2, 3, 1)
estrella_B = Estrella(4, 4, 4)
estrella_C = Estrella(-3, -1, 0)

print("Coordenadas de Estrella 1:", estrella_A)
print("Coordenadas de Estrella 2:", estrella_B)
print("Coordenadas de Estrella 2:", estrella_C)
print("Galaxia de Estrella 1:", estrella_A.galaxia())
print("Galaxia de Estrella 2:", estrella_B.galaxia())
print("Galaxia de Estrella 2:", estrella_C.galaxia())
print("Distancia entre Estrella 1 y Estrella 2:", estrella_A.distancia(estrella_B))
print("Distancia entre Estrella 1 y Estrella 2:", estrella_A.distancia(estrella_C))
print("Distancia entre Estrella 1 y Estrella 2:", estrella_B.distancia(estrella_C))

