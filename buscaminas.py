import os
tablero=[[".",".",".",".","."],
         [".",".",".",".","."],
         [".",".",".",".","."],
         [".",".",".",".","."],
         [".",".",".",".","."]]

posicionesDeMinas=[[".",".",".",".","."],
                   ["m","m","m",".","."],
                   ["m",".","m",".","."],
                   ["m","m","m",".","."],
                   [".",".",".",".","."]]
posF=0
posC=0
columnas=0
filas=0
caracterCursor="a"
caracterActual="."
caracterVacio=" "
caracterMina="m"
caracterSuelo="."

def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for x in range(len(matriz[0])):
            print(matriz[i][x],end="")
        print(" ")

def cuandoSonCero():
    print("xd")

def imprimirCursor(matriz,caracter,posC,posF):
    matriz[posF][posC]=caracter

def detectarCuantasMinasHayAlrededor(matrizMinas):
    global posC
    global posF
    global caracterActual
    global tablero
    global columnas
    global filas
    minas=0
    # x.. #
    # .j. #
    # ... # VERIFICADO
    posCT = posC 
    posfT = posF
    if posfT-1>=0 and posCT-1>=0:
        posCT=posCT-1
        posfT=posfT-1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # .x. #
    # .j. #
    # ... # VERIFICADO
    posCT = posC
    posfT = posF
    if posfT-1>0:
        posfT=posfT-1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ..x #
    # .j. #
    # ... # VERIFICADO
     
    posCT = posC
    posfT = posF   
    if  posfT-1>0 and posCT+1<columnas:       
        posCT=posCT+1
        posfT=posfT-1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ... #
    # .jx #
    # ... # VERIFICADO
    posCT = posC
    posfT = posF   
    if  posCT+1<columnas:       
        posCT=posCT+1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ... #
    # .j. #
    # ..x #  VERIFICADO
    posCT = posC
    posfT = posF   
    if  posfT+1<filas and posCT+1<columnas:       
        posCT=posCT+1
        posfT=posfT+1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ... #
    # .j. #
    # .x. # VERIFICADO
    posCT = posC
    posfT = posF   
    if  posfT+1<filas:       
        posfT=posfT+1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ... #
    # .j. #
    # x.. # VERIFICADO
    posCT = posC
    posfT = posF   
    if  posfT+1<filas and posCT-1>=0:       
        posfT=posfT+1
        posCT=posCT-1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1
    # ... #
    # xj. #
    # ... #
    posCT = posC
    posfT = posF   
    if  posCT-1>=0:       
        posCT=posCT-1
        if matrizMinas[posfT][posCT]==caracterMina:
            minas=minas+1

    tablero[posF][posC]=str(minas)
    caracterActual=str(minas)

def descrubirUbicacion(matrizMinas):
    global caracterActual
    if matrizMinas[posF][posC]==caracterSuelo:
        detectarCuantasMinasHayAlrededor(posicionesDeMinas)
    if matrizMinas[posF][posC]==caracterMina:
        tablero[posF][posC]=caracterMina
        caracterActual = caracterMina
        
def moverseEnElTablero():
    global posF
    global posC
    global caracterActual
    posCanterior=posC
    posFanterior=posF  

    """
    print("actual")
    print("col->"+str(posC),end="")
    print("fil->"+str(posF))
    print("anterior")
    print("col->"+str(posCanterior),end="")
    print("fil->"+str(posFanterior))
    print("car-> "+str(caracterActual))
    print("Direccion ->",end="")
    """
    direccion = str(input())
    imprimirCursor(tablero,caracterActual,posC,posF)
    if direccion=="a":
        if posC<=0:
            posC=columnas-1
        else:
            posC=posC-1
    if direccion=="d":
        if posC>=columnas-1:
            posC=0
        else:
            posC=posC+1
    if direccion=="w":
        if posF<=0:
            posF=filas-1
        else:
            posF=posF-1
    if direccion=="s":
        if posF>=filas-1:
            posF=0
        else:
            posF=posF+1
    if direccion=="x":
        descrubirUbicacion(posicionesDeMinas)
    else:
        caracterActual=tablero[posF][posC]
    
    imprimirCursor(tablero,caracterCursor,posC,posF)
    
def juego():
    global columnas
    global filas
    columnas = len(tablero[0])
    filas = len(tablero)
    print(filas)
    print(columnas)
    while True:
        os.system("cls")
        imprimirMatriz(tablero)
        moverseEnElTablero()

if __name__ == "__main__":
    juego()
        
