def main():
    cilindraje = int(input("======================================\n"
                           "           CATALOGO BAJAJ\n"
                           "======================================\n"
                           "   (1)-. Bajo cilindraje\n"
                           "   (2)-. Medio cilindraje\n"
                           "   (3)-. Alto cilindraje\n"
                           "======================================\n"
                           "Ingrese la opción de cilindraje: "))
    
    print("\n" * 50)  # Simula Limpiar Pantalla

    if cilindraje == 1:
        opmoto = int(input("======================================\n"
                           "           BAJO CILINDRAJE\n"
                           "======================================\n"
                           "   (1)-. BOXER 100 - $6.800.000\n"
                           "   (2)-. DISCOVER 125 - $8.000.000\n"
                           "   (3)-. BOXER 150X - $9.300.000\n"
                           "======================================\n"
                           "Ingrese la opción de moto: "))
    elif cilindraje == 2:
        opmoto = int(input("======================================\n"
                           "           MEDIO CILINDRAJE\n"
                           "======================================\n"
                           "   (4)-. PULSAR NS 200 - $12.000.000\n"
                           "   (5)-. PULSAR N 250 - $14.200.000\n"
                           "   (6)-. DOMINAR 250 - $16.500.000\n"
                           "======================================\n"
                           "Ingrese la opción de moto: "))
    elif cilindraje == 3:
        opmoto = int(input("======================================\n"
                           "           ALTO CILINDRAJE\n"
                           "======================================\n"
                           "   (7)-. DOMINAR 400 R - $19.400.000\n"
                           "   (8)-. DOMINAR 400 PRO - $19.800.000\n"
                           "   (9)-. DOMINAR 400 TOURING - $20.400.000\n"
                           "======================================\n"
                           "Ingrese la opción de moto: "))
    else:
        print("Opción no válida")
        return

    print("\n" * 50)  # Simula Limpiar Pantalla

    if opmoto == 1:
        moto = "BOXER 100"
    elif opmoto == 2:
        moto = "DISCOVER 125"
    elif opmoto == 3:
        moto = "BOXER 150X"
    elif opmoto == 4:
        moto = "PULSAR NS 200"
    elif opmoto == 5:
        moto = "PULSAR N 250"
    elif opmoto == 6:
        moto = "DOMINAR 250"
    elif opmoto == 7:
        moto = "DOMINAR 400 R"
    elif opmoto == 8:
        moto = "DOMINAR 400 PRO"
    elif opmoto == 9:
        moto = "DOMINAR 400 TOURING"
    else:
        print("Opción no válida")
        return

    nombre = input("=====================================================\n"
                   "           ESCRIBE TU NOMBRE COMPLETO\n"
                   "=====================================================\n"
                   "Nombre: ")
    
    print("\n" * 50)  # Simula Limpiar Pantalla

    num_documento = input("=====================================================\n"
                          "           ESCRIBE TU NUMERO DE DOCUMENTO\n"
                          "=====================================================\n"
                          "Número de documento: ")
    
    print("\n" * 50)  # Simula Limpiar Pantalla

    direccion = input("=====================================================\n"
                      "           ESCRIBE TU DIRECCIÓN DE RESIDENCIA\n"
                      "=====================================================\n"
                      "Dirección: ")
    
    print("\n" * 50)  # Simula Limpiar Pantalla

    print("======================================================================")
    print("           MUCHAS GRACIAS POR ADQUIRIR TU MOTO CON NOSOTROS")
    print("                   BIENVENIDO A LA FAMILIA BAJAJ")
    print("======================================================================")
    print(f"                {nombre}")
    print(f"                            {num_documento}")
    print(f"                            {direccion}")
    print(f"                            {moto}")
    print("======================================================================")
    print("                  GRACIAS POR CONFIAR EN NOSOSTROS")
    print("======================================================================")

if __name__ == "__main__":
    main()