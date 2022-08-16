# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
CABECERA  = 0   # Inicio o seccion de la tabla, con el nombre de la
                # sección.
MENSAJE   = 1   # Mensaje simple en pantalla (Sin variables).
RESULTADO = 2   # Mensaje con formato (Incluye variables).
 
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "METODO DE CRAMER"
MENSAJE_SOLUCION = "SOLUCIONES"
 
MENSAJE_ECUACION = '''
         a11(x1) + a12(x2) = c1
         a21(x1) + a22(x2) = c2
'''
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NÚMEROS"
 
 
# Declaracion de funciones:
def matriz_nula(filas, columnas):
    
    Matriz = []
 
    # Se agregan los elementos a la Matriz
    for elemento in range(filas):
        Matriz.append ([0] * columnas)
    return Matriz
 
def imprimir_mensaje(mensaje,tipo):
    
    if tipo == CABECERA:
        print(CADENA_VACIA.center(ANCHO,RELLENO1))
        # Imprime el Inicio o seccion de la tabla, con el nombre 
        # de la sección.
        print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
 
    elif tipo == MENSAJE:
        # Imprime un Mensaje simple en pantalla (Sin variables)
        print(mensaje.center(ANCHO,RELLENO2))
 
    elif tipo == RESULTADO:
        # Imrprime un Mensaje con formato (Incluye variables)
        print(mensaje)
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
def metodo_cramer():
   
   filas, columnas = 2, 2
 
   M = matriz_nula(filas, columnas)
 
   for fila in range(filas):
        for col in range(columnas):
            M[fila][col]=float(input("Dato a%d%d: " %(fila+1,col+1)))
        #Se agregan Los terminos independientes C1 y C2
        M[fila].append(float(input("Dato c%d : " %(fila+1))))
        print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
   # Se almacenan las posiciones de la Matriz en las variables 
   # correspondientes
 
   # Ecuacion 1
   a11 = M[0][0]
   a12 = M[0][1]
   c1  = M[0][2]
 
   # Ecuacion 2
   a21 = M[1][0]
   a22 = M[1][1]
   c2  = M[1][2]
 
   # Puede resolverse usando la regla de Cramer:
 
   x1 = (c1*a22 - c2*a12)/(a11*a22 - a12*a21)
   x2 = (c2*a11 - c1*a21)/(a11*a22 - a12*a21)
 
   RESPUESTA = ">>> x1 = %4.2f y x2 = %4.2f" %(x1, x2)
 
   imprimir_mensaje(MENSAJE_SOLUCION, MENSAJE)
   imprimir_mensaje(RESPUESTA, RESULTADO)
 
 
def main():
    
    imprimir_mensaje(MENSAJE_INICIAL , CABECERA)
    imprimir_mensaje(MENSAJE_ECUACION, MENSAJE)
    metodo_cramer()
 
 
# Inicio del programa:
main()