# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "TIEMPO DE ENCUENTRO DE 2 VEHICULOS"
 
# Mensajes de Solicitud de Datos
SOLICITAR_DISTANCIA  = ">>> Distancia de Separacion  : "
SOLICITAR_VELOCIDAD1 = ">>> Velocidad del Vehiculo 1 : "
SOLICITAR_VELOCIDAD2 = ">>> Velocidad del Vehiculo 2 : "
 
# Mensajes de Error
ERROR_VELOCIDADES = "ERROR: Tiempo de encuentro INFINITO"
 
 
# Declaracion de variables
tiempo = 1
distancia = 0.0
velocidad1, velocidad2 = 0.0, 0.0
 
# Formato de Salida Final en Pantalla
formato_respuesta = "TIEMPO: %4.2f segundos"
 
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
 
# Inicio del Programa:
distancia  = float( input(SOLICITAR_DISTANCIA))
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
velocidad1 = float( input(SOLICITAR_VELOCIDAD1))
velocidad2 = float( input(SOLICITAR_VELOCIDAD2))
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
if velocidad1 > 0 and velocidad2 > 0 :
 
    tiempo = distancia/(velocidad1 + velocidad2)
 
    # Se muestra el mensaje en Pantalla
    print(formato_respuesta.center(ANCHO,RELLENO2) %(tiempo))
else:
    print(ERROR_VELOCIDADES)
 
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))