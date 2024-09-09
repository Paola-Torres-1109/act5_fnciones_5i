print("funciones creadas por el usuario")
#Las funciones

#Listas
print("--Listas--")
def Mi_lista():
    amigos=["jus","wichito","emi"]
    for pao in amigos:
        print(pao)
# llamadas  a funciones 
Mi_lista()

#tuplas
print("")
print("--Tuplas--")
arcoiris = ("rojo","naranja","amarillo","verde")
for elcolor in arcoiris:
    print(elcolor)

#conjuntos
print("")
print("--Conjuntos--")
amigos = {"wichito", "emi", "jus"}
for i in amigos:
    print(i)


#diccionarios
print("")
print("--Diccionario--")
datos = {
    "nombre": "Paola",
    "edad": "17",
    "cumpleaños": "28 de enero",
    "ig": "iiam_.paoo"
}
for i in datos:
    print(datos[i])