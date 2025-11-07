from coordenadas import*

def test_calcular_distancia (coordenada1,coordenada2):
    distancia = calcular_distancia(coordenada1, coordenada2)
    print("La distancia es",distancia)

def media_long_lat(lista_coordenadas):
    resultado = calcular_media_coordenadas(lista_coordenadas)
    print("La latitud media y la longitud media es",resultado)

def main():
    coordenada1 = Coordenadas(36.135051666002795, -5.843455923196172)
    coordenada2 = Coordenadas(36.72460010332263, -5.931456684613025)
    test_calcular_distancia(coordenada1,coordenada2)
    
    lista_coordenadas = [coordenada1,coordenada2]

    media_long_lat(lista_coordenadas)
    


if __name__ == "__main__":
    main()