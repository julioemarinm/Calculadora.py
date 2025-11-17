print("=== CALCULADORA BÁSICA ===")
print("Selecciona una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

op = input("Ingresa el número de la operación: ")

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if op == "1":
    print("Resultado:", num1 + num2)

elif op == "2":
    print("Resultado:", num1 - num2)

elif op == "3":
    print("Resultado:", num1 * num2)

elif op == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: no se puede dividir entre cero")

else:
    print("Opción no válida")
