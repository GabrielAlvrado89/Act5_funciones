print("Ejemplos de funciones")
# declarando funciones
def hola():
    print("Alguien uso la función hola")
def chat(menso):
    print(f"Chat {menso}")
def ellacontesta(menso):
    print(f"Chat {menso}")
def escribenombre(ap,n):
    print(f"Tu nombre completo es : {n} {ap}")

def suma(a,b): 
    s=a+b
    return s
#################
def resta(a,b): 
    s=a-b
    return s
#################
def multiplicacion(a,b): 
    s=a*b
    return s
##################
def division(a,b): 
    s=a/b
    return s
## llamadas a funciones 
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribenombre("Alvarado","Angel")
print("Operaciones básicas")
## Suma
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")
## Resta
c3=int(input("Ingresa un numero"))
c4=int(input("Ingresa un numero"))
damesuma=resta(c3,c4)
print(f"La resta de {c3} - {c4} = {damesuma}")
## Multiplicacion 
c5=int(input("Ingresa un numero"))
c6=int(input("Ingresa un numero"))
damesuma=multiplicacion(c5,c6)
print(f"La multiplicacion de {c1} x {c2} = {damesuma}")
## Division
c7=int(input("Ingresa un numero"))
c8=int(input("Ingresa un numero"))
damesuma=division(c7,c8)
print(f"La division de {c7} / {c8} = {damesuma}")