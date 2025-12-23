class Auto: # auto_1 = Auto()
    CANTIDAD_DE_RUEDAS = 4

    def __init__(self, color, modelo, marca):
        # Los atributos que defino aca son de INSTANCIA
        if color == "blanco":
            raise ValueError("No se permite color blanco")
        self.color = color
        self._modelo = modelo
        self.marca = marca

    def ver_info(self): # METODOS DE INSTANCIA
        print(f"El auto es de color {self.color} y es un {self.marca} - {self._modelo}")
    
    @classmethod
    def obtener_cantidad_ruedas(cls): # cls = class, en este caso seria como recibir Auto.
        return cls.CANTIDAD_DE_RUEDAS

    @staticmethod
    def encender():
        print("Encendio")


auto = Auto("rojo", "ford", "Ka")
auto_1 = Auto("Azul", "Kardian", "Renault")
auto_1._modelo = "Kwid"
print(auto_1._modelo)
print(auto.obtener_cantidad_ruedas(), auto_1.obtener_cantidad_ruedas())
auto.encender()
Auto.encender()
