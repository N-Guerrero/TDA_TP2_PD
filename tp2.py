#OPT(i) = min(
#"" si i= |seg|,
#seg[i:j]+" "+opt(j) para el primer j∈(i+1,∣s∣]tal que s[i:j]∈D y opt(j)!=None
#) 
import sys
import time

def cargar_palabras(path_archivo):
    diccionario = []
    with open(path_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabra = linea.strip().lower()
            if palabra:
                diccionario.append(palabra)
    return diccionario



def segmentar_texto(s, diccionario):
    n = len(s)
    opt = [None] * (n + 1)
    opt[n] = ""  
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            palabra = s[i:j]
            if palabra in diccionario and opt[j] is not None:
                opt[i] = palabra if opt[j] == "" else palabra + " " + opt[j]
                break 
    return opt[0]



def main(archivo1,archivo2):
    
    diccionario=cargar_palabras(archivo1)
    mensajes=cargar_palabras(archivo2)
    dicc_set=set(diccionario)
    
    
    total_chars = sum(len(m) for m in mensajes)

    inicio = time.perf_counter()
    for mensaje in mensajes:
        
        resultado=segmentar_texto(mensaje, dicc_set)
        print(resultado)
    fin = time.perf_counter()
    duracion = fin - inicio
    #print(f"chars:{total_chars},time:{duracion:.8f},dicc:{archivo1},mensajes:{archivo2} \n")
    #with open("tiempos_totales.txt", "a", encoding="utf-8") as salida:
     #  salida.write(f"chars:{total_chars},time:{duracion:.8f},dicc:{archivo1},mensajes:{archivo2} \n")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python tp2.py <diccionario.txt> <mensajes.txt>")
    else:
        archivo_diccionario = sys.argv[1]
        archivo_mensajes = sys.argv[2]
        main(archivo_diccionario, archivo_mensajes)


