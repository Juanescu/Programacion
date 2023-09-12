#Ejercicio 1 en inglés

x = 0
while x <= 30:
    x += 1
    if x == 15:
        break
    if x ==4 or x==6 or x==10:
        print(f"El valor {x} de x fue omitido")
        continue
    else:
        print(f"El valor del ciclo es:  {x}")

print(f"Se rompió la ejecucuión del bucle cuando x valia: {x}")



#Ejercicio 1

lines = []
while True:
    line = input("Ingrese una línea de texto (deje en blanco para finalizar): ")
    if not line:
        break
    lines.append(line)

for linea in lines:
    print(linea.upper())



#Ejercicio 2

balance = 0
while True:
    operation=input("Ingrese una operación (D para depósito, R para retiro, o línea vacía para salir): ")
    if operation == "":
        break

    if operation == "D":
        amount=int(input("Ingrese el monto a depositar: "))
        if amount < 0:
            print("Ingrese un número mayor a 0")
            continue
        balance += amount
        print("D ",amount)
    elif operation == "R":
        amount=int(input("Ingrese el monto a retirar: "))
        if amount < 0:
            print("Ingrese un número mayor a 0")
            continue
        if amount > balance:
            print("El saldo que quiere retirar es mayor al que posee en la cuenta")
            continue
        balance-= amount
        print("R ",amount)
    else:
        print("Operación no válida")

print ("El saldo de su cuenta es de: ",balance)



#Ejercicio 3

cantprim=0

while True:
    num= int(input("Ingrese un numero mayor o igual a 1(0 para salir):"))
    if num==0:
        break
    if num >= 1:
        esPrimo=True
        for i in range(2, num):
            if num % i == 0:
                esPrimo=False
                break
        if esPrimo:
            cantprim+=1
    else:
        print("El numero debe ser mayor o igual que 1")
print(f'La cantidad de numeros primos es: {cantprim}')



#Ejercicio 4

first_year = int(input("Ingrese el primer año: "))
second_year = int(input("Ingrese el segundo año: "))
x = range(first_year, second_year+1)
for i in x:
    if i % 10 == 0:
        print(f"El año {i}, es multiplo de 10")
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                print(f"El año {i}, es un año biciesto")  
            else:
                print(f"El año {i}, NO es un año biciesto")  
        else:
            print(f"El año {i}, es un año biciesto")



#Ejercicio 5

for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number)



#Ejercicio 6

numbers =[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_number = int(input("Ingrese un numero para ser buscado: "))

for num in numbers:
    if num == target_number:
        print(f"Se encontró el numero: {target_number}")
        break
else:
    print(f"El numero {target_number} no fue encontrado")



#Ejercicio 7

answer = -1
print("Eliga una opción")
print("1-Primera opción \n2-Segunda opción \n3-Tercera opción")
while answer != 0:
    answer = int(input("> "))
    if answer==0:
        print("\nprograma finalizado")
        break
    elif answer==1:
        print("\nHas elegido la opcion 1")
    elif answer == 2:
        print("\nHas elegido la opcion 2")
    elif answer == 3:
        print("\nHas elegido la opcion 3")
    else:
        print("\nNo has elegido ninguna opción") 
    print("\nIngrese otra opción")

