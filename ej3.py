def magia_numerica(lista_numeros):

    lista_sin_duplicados = list(set(lista_numeros))

    lista_ordenada = sorted(lista_sin_duplicados, reverse=True)

    lista_pares = [num for num in lista_ordenada if num % 2 == 0]

    suma_total = sum(lista_pares)

    lista_final = [suma_total] + lista_pares
    
    return lista_final

numeros = [7, 3, 0, 2, 8, 1, 4, 9, 6]
resultado = magia_numerica(numeros)
print(resultado)
