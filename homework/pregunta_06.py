"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():

    df = pd.read_csv(
        r'C:\Users\ASUS\Desktop\Analitica_Curso\Laboratorios\LAB-02-pandas-mherrerao\files\input\tbl1.tsv',
        sep='\t'
    )

    valores_unicos = df["c4"].str.upper().unique()
    lista_ordenada = sorted(valores_unicos)

    return lista_ordenada


print(pregunta_06())

    #"""
    #Retorne una lista con los valores unicos de la columna `c4` del archivo
    #`tbl1.csv` en mayusculas y ordenados alfabéticamente.

    #Rta/
    #['A', 'B', 'C', 'D', 'E', 'F', 'G']

    #"""
