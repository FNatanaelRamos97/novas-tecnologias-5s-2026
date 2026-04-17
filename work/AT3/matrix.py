def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    # criando uma lista vazia
    transposta = []

    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    return transposta

def multiplicar_matriz(matriz_a, matriz_b):
    linhas_a = len(matriz_a)
    colunas_a = len(matriz_a[0])
    
    linhas_b = len(matriz_b)
    colunas_b = len(matriz_b[0])

    if colunas_a != linhas_b:
        print("Erro: não é possivel multiplicar as matrizes")
        return None

    resultado = []

    for i in range(linhas_a):
        linha_resultado = []

        for j in range(colunas_b):
            soma = 0

            for k in range(colunas_a):
                soma += matriz_a[i][k] * matriz_b[k][j]
            
            linha_resultado.append(soma)

        resultado.append(linha_resultado)

    return resultado

    