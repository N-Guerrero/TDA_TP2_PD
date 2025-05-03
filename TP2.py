#OPT(i) = min(
#"" si i= |seg|,
#seg[i:j]+" "+opt(j) para el primer j∈(i+1,∣s∣]tal que s[i:j]∈D y opt(j)!=None
#) 
def cargar_palabras(path_archivo):
    diccionario = []
    with open(path_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabra = linea.strip().lower()
            if palabra:
                diccionario.append(palabra)
    return diccionario



def segmentar_texto(s, diccionario, memo, i=0):
    if i in memo:
        return memo[i]
    if i == len(s):
        return ""

    for j in range(i + 1, len(s) + 1):
        palabra = s[i:j]
        if palabra in diccionario:
            resto = segmentar_texto(s, diccionario, memo, j)
            if resto is not None:
                memo[i] = palabra if resto == "" else palabra + " " + resto
                return memo[i]

    memo[i] = None
    return None


def main(archivo1,archivo2):
    diccionario=cargar_palabras(archivo1)
    mensajes=cargar_palabras(archivo2)
    dicc_set=set(diccionario)
    
    for mensaje in mensajes:
        memoria={}
        resultado=segmentar_texto(mensaje,dicc_set,memoria)
        print(resultado)



