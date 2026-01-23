


from mi_programa_clientes import Cliente, ClienteVIP

def mostrar_demo():
    print("=========================================")
    print("DEMOSTRACIÓN DE LA CLASE CLIENTE")
    print("=========================================")

   
    cliente1 = Cliente("Ana López", "ana.l@mail.com", "Argentina")
    cliente2 = Cliente("Luis Perez", "l.perez@otro.net")  
    clientevip3 = ClienteVIP("Carlos Gómez", "c.gomez@vip.com", "Chile")

   
    print("\n--- Representación de Objetos (__str__) ---")
    print(cliente1)
    print(cliente2)
    print(clientevip3)

    
    print("\n--- Uso de Métodos ---")

 
    cliente1.agregar_compra("Libro de Python", 25.50)
    cliente1.agregar_compra("Mouse inalámbrico", 40.00)
    total1 = cliente1.calcular_total_gastado()
    print(f"* Total gastado por {cliente1.nombre}: ${total1:.2f}")

    
    monto_original = 100.00
    monto_descontado = clientevip3.aplicar_descuento(monto_original)
    print(f"\n* Monto Original: ${monto_original}")
    print(f"* Monto con Descuento VIP ({clientevip3.descuento_fijo*100:.0f}%): ${monto_descontado:.2f}")

    clientevip3.agregar_compra("Monitor 27'", monto_descontado) 
    total3 = clientevip3.calcular_total_gastado()
    print(f"* Total gastado por {clientevip3.nombre}: ${total3:.2f}")


    print("\n--- Acceso a Atributos ---")
    print(f"El ID de {cliente2.nombre} es: {cliente2.id_cliente}")
    print(f"El país de {cliente1.nombre} es: {cliente1.pais}")


if __name__ == "__main__":
    mostrar_demo()


    