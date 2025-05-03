#OPT(i) = min(
#"" si i= |seg|,
#seg[i:j]+" "+opt(j) para el primer j∈(i+1,∣s∣] tal que s[i:j]∈D y opt(j)!=None
#) 
def cargar_palabras(path_archivo):
    diccionario = []
    with open(path_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabra = linea.strip().lower()
            if palabra:
                diccionario.append(palabra)
    return diccionario



# def segmentar_texto(seg, diccionario):
#     from functools import lru_cache

#     diccionario = set(diccionario)  # Para búsqueda rápida

#     @lru_cache(maxsize=None)
#     def dp(i):
#         if i == len(seg):
#             return ""  # Caso base: cadena vacía

#         for j in range(i + 1, len(seg) + 1):
#             palabra = seg[i:j]
#             if palabra in diccionario:
#                 resto = dp(j)
#                 if resto is not None:
#                     if resto == "":
#                         return palabra
#                     else:
#                         return palabra + " " + resto

#         return None  # No se pudo segmentar desde i

#     return dp(0)


def main(archivo1,archivo2):
    diccionario=cargar_palabras(archivo1)
    mensajes=cargar_palabras(archivo2)


