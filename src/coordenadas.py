from typing import NamedTuple
import math


Coordenadas = NamedTuple("Coordenadas", [("latitud",float),("longitud",float)])


def calcular_distancia(coordenada1:Coordenadas, coordenada2:Coordenadas)->Coordenadas:
    calculo=math.sqrt((coordenada2.latitud-coordenada1.latitud)**2 + (coordenada2.longitud-coordenada1.longitud)**2)
    return calculo


def calcular_media_coordenadas(coordenadas:list[Coordenadas])-> Coordenadas:

    n = len(coordenadas)
    suma_latitud = 0
    suma_longitud = 0
    for coordenada in coordenadas:
      
        suma_latitud += coordenada.latitud
        suma_longitud += coordenada.longitud
    
    return Coordenadas(suma_latitud/n, suma_longitud/n)
    

    
    

    

