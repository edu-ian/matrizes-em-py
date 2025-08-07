print("Digite a ordem da matriz quadrada (ex: 2 para 2x2, 3 para 3x3):")
n = int(input())

print("\nDigite os valores da MATRIZ A:")
A = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

print("\nDigite os valores da MATRIZ B:")
B = []
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"B[{i}][{j}]: "))
        linha.append(valor)
    B.append(linha)

print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nMultiplicando as matrizes passo a passo...")
resultado = []
for i in range(n):
    linha_resultado = []
    for j in range(n):
        soma = 0
        for k in range(n):
            mult = A[i][k] * B[k][j]
            soma += mult
            print(f"A[{i}][{k}] * B[{k}][{j}] = {A[i][k]} * {B[k][j]} = {mult} | Soma parcial: {soma}")
        linha_resultado.append(soma)
    resultado.append(linha_resultado)

print("\nMatriz Resultado (A x B):")
for linha in resultado:
    print(linha)
