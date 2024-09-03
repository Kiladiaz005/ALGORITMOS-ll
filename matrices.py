def dot(A,B):
    if len(A) == len(B):
        suma = 0
        for i in range(len(A)):
            suma += A[i]*B[i]
        return suma
    else:
        print("error, los tamaños de los vectores deben ser iguales")
        return 0
def cross(A,B):
    resultado = [0,0,0]
    if len(A) == 3 and len(B) == 3:
        resultado[0] = A[1]*B[2]-A[2]*B[1]
        resultado[1] = -A[0]*B[2]+A[2]*B[0]
        resultado[2] = A[0]*B[1]-A[1]*B[0]
    else:
        print("El tamaño de los vectores debe ser de 3 elementos")
    return resultado
def mat_mult(A,B):
    resultado =[]
    for i in range(len(A)):
        resultado.append([])
    if len(A[0]) == len(B):
        for i in range(len(B[0])):
            for j in range(len(A)):
                vertical = []
                for k in range(len(B)):
                    vertical.append(B[k][i])
                resultado[j].append(dot(A[j],vertical))
    else:
        print("los tamaños no coinciden")
    return resultado
A = [1, 2, 3]
B = [1, 8, 89]
print(cross(A,B))