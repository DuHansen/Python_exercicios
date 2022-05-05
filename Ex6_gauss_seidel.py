from numpy import array, zeros
import cmath

def Gauss_Seidel(matriz_aumentada, vetor):  # função do método 
    m = len(matriz_aumentada)
    n = len(matriz_aumentada[0])
    x = zeros((m))
    comp = zeros((m))
    error = []
    TOL = 0.0002  # erro tolerado
    maxit = 5000
    k = 0
    while k < maxit:
        suma = 0
        k = k + 1
        print(f'Iteração: {k}')
        for r in range(0, m):
            suma = 0
            for c in range(0, n):
                if (c != r):
                    suma = suma+matriz_aumentada[r, c] * x[c]
            x[r] = (vetor[r]-suma)/matriz_aumentada[r, r]
            print(f'x[{r}]: {x[r]}')
        del error[:]
        for r in range(0, m):
            suma = 0
            for c in range(0, n):
                suma = suma+matriz_aumentada[r, c] * x[c]
            comp[r] = suma
            dif = abs(comp[r]-vetor[r])
            error.append(dif)
            print(f'Erro em x[{r}] = {error[r]}')
        if all(i <= TOL for i in error) is True:
            break
    print(f'Com {k} iterações.')
    for c in range(0, m):
        print(f'x[{c}]: {round(x[c],4)}')

# Uso do método
matriz_aumentada = array([
    [3+3j,-1-1j,-1-1j],
     [-1-1j,3+3j,-1-1j],
     [-1-1j,-1-1j,3+3j]])
vetor = array([1,1,1,])
Gauss_Seidel(matriz_aumentada, vetor)
