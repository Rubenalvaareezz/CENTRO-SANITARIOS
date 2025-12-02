from coordenadas import *
from typing import NamedTuple
import csv

CENTROS = NamedTuple("centros",
                     [("nombre", str),
                      ("localidad", str ),
                      ("coordenadas", Coordenadas),
                      ("estado", str),
                      ("num_camas", int),
                      ("tiene_acceso_discapacitados", bool),
                      ("tiene_uci", bool)])

def lee_centros(fichero):
    with open(fichero, encoding="utf-8") as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for nombre, localidad, coordenadas, estado, num_camas, tiene_acceso_discapacitados, tiene_uci in lector:
            coordenadas = Coordenadas(coordenadas)
            num_camas = int(num_camas)
            tiene_acceso_discapacitados = bool(tiene_acceso_discapacitados)
            tiene_uci = bool(tiene_uci)
            atributos = CENTROS(nombre, localidad, coordenadas, estado, num_camas, tiene_acceso_discapacitados, tiene_uci)
            res.append(atributos)
    return res
        