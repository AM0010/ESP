# Función para sumar dos números
def sumar(x, y):
    return x + y

# Función para restar dos números
def restar(x, y):
    return x - y

def main():
    print("Calculadora Básica")
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")

    while True:
        seleccion = input("Ingresa el número de la operación deseada (1/2): ")

        if seleccion in ['1', '2']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue

            if seleccion == '1':
                print(f"El resultado de la suma es: {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"El resultado de la resta es: {restar(num1, num2)}")

            otra = input("¿Quieres hacer otra operación? (sí/no): ")
            if otra.lower() != 'sí':
                print("¡Gracias por usar la calculadora!")
                break
        else:
            print("Selección inválida. Por favor, elige 1 o 2.")

if __name__ == "__main__":
    main()
    