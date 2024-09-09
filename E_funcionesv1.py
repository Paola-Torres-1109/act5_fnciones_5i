print("Manejo de funciones v1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")

def Mensa(msg):
    print(msg)

def EscribeNC(Nombre,Apellido):
    print(Nombre, Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")

def suma2num(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de: ", s
# llamando a la funcion
hola_mundo()
Mensa("hola whatsapp") #llama a mensa con 1 parametro
Mensa("El profe me sorprendio enviando mensajes")#llama a mensa con 1 parametro
EscribeNC("Pao", "Torres")
print("")
print("Funciones que regresan valores")
print(suma2num(7,3))
print(suma2num(15,45))
