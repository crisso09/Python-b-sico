with open("comidas.csv", "w") as inventario:
    tipos=int(input("¿Cuántos tipos de comidas vas a cocinar hoy>:"))
    for i in range(tipos):
        platos=input("Qué plato vas a poner?: ")
        cantidad=input("Cuántos raciones son?: ")
        precio=input("Cuánto cuesta este plato?: ")
        registro=f"#{str(i+1)}; {platos}; {cantidad}; ${precio}\n"
        inventario.write(registro)
    inventario.close()
with open("comidas.csv", "r") as inventario:
    for l in inventario:
        print(l)
    inventario.close()
with open("mesita.csv", "w") as llevar:
    mesa=f"producto; Cantidad_m\n"
    llevar.write(mesa)
    llevar.close()
