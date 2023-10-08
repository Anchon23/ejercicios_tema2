texto_bruto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

texto_formateado = texto_bruto.replace("#", "\n")

lineas = texto_formateado.split("\n")
lineas = [linea + "." for linea in lineas]
lineas = [linea.capitalize() for linea in lineas]
print(lineas[0] + '...')

for linea in lineas[1:]:
    print(f'\t· {linea}')

texto_final = "\n".join(lineas)
