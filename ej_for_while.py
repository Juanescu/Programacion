#Ejercicio 1 For

print ("--Ejercicio 1--")

alfabeto= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
corrimiento= int(input("Ingrese el numero de lugares a correr: "))
for i in range(5):
    mensaje_encriptado= ""
    mensaje= input("Ingrese el mensaje a encriptar: ").upper()
    for letra in mensaje:
        if letra in alfabeto:            
            lugar = alfabeto.index(letra)
            nuevo_lugar = (lugar + corrimiento)%27
            mensaje_encriptado = mensaje_encriptado+ alfabeto[nuevo_lugar]
        else:
            mensaje_encriptado += letra
    print(mensaje_encriptado)

print ("--Fin Ejercicio 1--")
print ("  ")

#Ejercicio 2 While

print ("--Ejercicio 2--")

num = 1
sumapar = 0
sumaimpar = 0
while num != 0:
    numing = input("Ingrese números enteros positivos o ingrese 0 para finalizar: ")
    if int(numing) != 0:
        par = 0
        impar = 0
        for n in numing:
            n1 = int(n)%2
            if n1 == 0:
                par += 1
                sumapar += 1
            else:
                impar += 1
                sumaimpar += 1
        print("El número ingresado, tiene ", par," de números pares y ",impar," de números impares.")
    else:
        num = int(numing)
print("La cantidad de numeros ingresados es de: ", sumapar," números pares y ", sumaimpar," números impares.")

print("--Fin Ejercicio 2--")