class letra_dni:
    letras = ["T", "R", "w", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    longitud = [*range(0, len(letras))]
    tabla = dict(zip(longitud, letras))
    
    def __init__(self, numero):
        self.numero = int(numero)

    def calcular_letra(self):
        try:
            return letra_dni.tabla[self.numero % len(letra_dni.letras)]
        except:
            "Ha ocurrido un error calculando la letra"