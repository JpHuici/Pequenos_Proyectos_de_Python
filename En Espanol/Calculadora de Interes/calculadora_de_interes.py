# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "INTERES COMPUESTO (USD)"
 
# Mensajes de Solicitud de Datos
SOLICITUD_CAPITAL = ">>> Capital Inicial: "
SOLICITUD_INTERES = ">>> Porcentaje de interes: "
SOLICITUD_TIEMPO =  ">>> Tiempo en Años: "
 
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
 
 
# Declaracion de variables
Capital, Interes, Tiempo = 0, 0, 0
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = "CAPITAL TOTAL: %4.2f"
 
 
# Encabezado del Programa
#  Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
 
# Inicio del Programa:
while (Capital<0) or (Interes<=0) or (Interes>=100) or (Tiempo <=0):
    Capital = int(input(SOLICITUD_CAPITAL))
    Interes = int(input(SOLICITUD_INTERES))
    Tiempo  = int(input(SOLICITUD_TIEMPO))
 
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
for Elemento in range(Tiempo):
    Capital = Capital * ( 1 + Interes/100)
 
# Se muestra el mensaje en Pantalla
print(Formato_Respuesta.center(ANCHO,RELLENO2) %(Capital))
 
 
# Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))