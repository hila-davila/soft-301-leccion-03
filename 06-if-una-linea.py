# CONDICIONAL DOBLE
# if condicion:
# sentencias 
# else:
# sentencias 

A = int (input("Ingrese el numero 01:"))
B = int (input("Ingrese el numero 02:"))

# if A > B:
M = A
# else: 
M = B

M = A if A > B else B
print ("El mayor es: " + str(M) )

# Migar el programa de pares e impares 

A =  int(input("Ingrese el valor de A:"))
R = A % 2

if R == 0:
     print ("Par")
     print ("Impar")

print ("par") if R == 0 else print ("Impar")
