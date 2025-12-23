

# cliente.py

class Cliente:
    # Atributo de Clase (opcional)
    # Contador para llevar un registro de cuántos clientes se han creado.
    _contador_clientes = 0

    def __init__(self, nombre, email, pais='No especificado'):
        """
        Método constructor para inicializar los atributos de instancia.
        Requisito: Usar init para definir uno o más atributos.
        """
        # Atributos de Instancia (mínimo 4)
        self.nombre = nombre
        self.email = email
        self.pais = pais  # Atributo inicializado con un valor por defecto si no se proporciona
        self.id_cliente = Cliente._generar_id()  # Asignación de ID
        self.historial_compras = []  # Inicializado como lista vacía

    @classmethod
    def _generar_id(cls):
        """
        Método de clase privado para generar un ID simple.
        Actualiza el contador de clientes.
        """
        cls._contador_clientes += 1
        return f"CLI-{cls._contador_clientes:04d}"

    def __str__(self):
        """
        Método magic __str__().
        Requisito: Usar str() para darle nombre a los objetos (representación en string).
        """
        return f"Cliente ID: {self.id_cliente}, Nombre: {self.nombre}, Email: {self.email}"

    # --- Métodos por fuera de los magic methods (Requisito: Mínimo 2) ---

    def agregar_compra(self, producto, monto):
        """
        Método 1: Registra una nueva compra en el historial.
        """
        compra = {"producto": producto, "monto": monto}
        self.historial_compras.append(compra)
        print(f"\n* Compra de {producto} por ${monto} agregada a {self.nombre}.")

    def calcular_total_gastado(self):
        """
        Método 2: Calcula la suma total de dinero gastado por el cliente.
        """
        total = sum(compra['monto'] for compra in self.historial_compras)
        return total

# --- Contenido Adicional Opcional (Herencia) ---

class ClienteVIP(Cliente):
    """
    Subclase que hereda de Cliente.
    """
    def __init__(self, nombre, email, pais='No especificado', descuento_fijo=0.10):
        super().__init__(nombre, email, pais)
        self.descuento_fijo = descuento_fijo

    def __str__(self):
        # Sobreescribe el método str() del padre
        return f"** Cliente VIP ID: {self.id_cliente}, Nombre: {self.nombre}, Descuento: {self.descuento_fijo*100:.0f}%"

    def aplicar_descuento(self, monto):
        """
        Método 3: Aplica el descuento VIP a un monto.
        """
        monto_con_descuento = monto * (1 - self.descuento_fijo)
        return monto_con_descuento
    

    
