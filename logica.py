import numpy as np

def calculo_batido (tortas: list):
    lista_tortas = np.array(tortas)
    tamaño_tortas = np.array([160, 260, 380, 500, 640, 800])
    resultado = int(round((lista_tortas*tamaño_tortas).sum()*1.03,0))
    return resultado

def calculo_jarabe (tortas: list):
    lista_tortas = np.array(tortas)
    cantidad_jarabe = np.array([210, 340, 500, 650, 830, 1120])
    resultado = (lista_tortas*cantidad_jarabe).sum()
    return resultado

def receta_batido (total_batido: int):
    receta = np.array([0.454401943, 0.26387371, 0.26387371, 0.004371585, 0.004371585, 0.009107468])
    resultado = total_batido*receta
    return resultado.tolist()

def receta_jarabe (total_jarabe: int):
    receta = np.array([0.753183154, 0.150636631, 0.037610186, 0.050244858, 0.008325171])
    resultado = total_jarabe*receta
    return resultado.tolist()