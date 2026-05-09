from calculadora import sumar, restar, multiplicar, dividir, potenciar

def pedir_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a, b

def menu():
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciación")
    print("0. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                a, b = pedir_numeros()
                print("Resultado:", sumar(a, b))

            case "2":
                a, b = pedir_numeros()
                print("Resultado:", restar(a, b))

            case "3":
                a, b = pedir_numeros()
                print("Resultado:", multiplicar(a, b))

            case "4":
                a, b = pedir_numeros()

                if b == 0:
                    print("No se puede dividir entre 0")
                else:
                    print("Resultado:", dividir(a, b))

            case "5":
                a, b = pedir_numeros()
                print("Resultado:", potenciar(a, b))

            case "0":
                print("Programa finalizado")
                break

            case _:
                print("Opción inválida")

if __name__ == "__main__":
    main()