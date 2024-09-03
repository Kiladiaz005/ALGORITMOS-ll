cantidad = int(input("Ingrese el tamaño de la población "))
datos = []
for i in range(cantidad):
    datos.append(float(input("Ingrese dato ")))
x_barra = sum(datos)/cantidad
varianza = 0
for i in range(cantidad):
    varianza += (datos[i]-x_barra)**2
varianza = varianza/cantidad
print("La varianza es igual a ",varianza)