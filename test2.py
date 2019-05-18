def saludo(nombre):
    if nombre == "Anny":
        print("Hola Anny")
        print("Anny are you OK?")
    elif nombre == "Cobrita":
        print("Hola Cobrita!")
        print("Creador de este codigo")
    else:
        print("Vos no sos Anny")
        print("Seguro estas OK")
        print(nombre + " tampoco creaste este codigo")

nombres=["Anny","Cobrita","Ro"]

for nombre in nombres:
    print("")
    saludo(nombre)
    print("")
    print("EL QUE SIGUE!")
