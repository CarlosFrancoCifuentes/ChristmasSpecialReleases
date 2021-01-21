from src.tabla_dni import letra_dni

class dni:
    
    longitud_dni = 9
    
    def __init__(self, full_dni):
        self.full_dni = str(full_dni)

    def verificar_longitud(self):
        if len(self.full_dni) == self.longitud_dni:
            return True
        else:
            return "Error: dni demasiado largo o corto"

    def verificar_letra(self):
        if self.full_dni[-1].isalpha() == True:
            letra_correcta = letra_dni(self.full_dni[:-1]).calcular_letra()
            if letra_correcta == self.full_dni[-1]:
                return self.full_dni
            else:
                return False
        if self.full_dni[0].isalpha() == True:
            letra_correcta = letra_dni(self.full_dni[1:]).calcular_letra()
            if letra_correcta == self.full_dni[0]:
                return self.full_dni
            else:
                return False
        else:
            return self.full_dni + letra_dni(self.full_dni).calcular_letra()

    def creador_dni(self):
        if dni.verificar_longitud(self) != True:
            return dni.verificar_longitud(self)
        resultado = dni.verificar_letra(self)
        if resultado == False:
            return "Error: la letra no es correcta"
        else:
            return self.full_dni
