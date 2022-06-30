import pandas as pd
import re

# Funciones auxiliares
NUMS = {"un":1, "dos":2, "tres":3,"cuatro":4,"cinco":5, "seis":6, "siete":7, "ocho":8, "nueve":9}

# showPerOfNull Imprime el porcentaje de de campos nulos de un data set
def showPerOfNull(df=pd.DataFrame, show=True):
    nils = (df.isnull().sum()/df.shape[0]) * 100
    if show:
        print(nils)
    else:
        return nils

# fillAmountVar Recorre las filas de un data frame y rellena los campos nulos con el valor extraido de la columna descripcion a partir de una expresion regular
# 
# data_row: fila del data frame
# reg_exp: expresion regular
# col: columna del data frame
def inputNumber(data_row=pd.DataFrame, reg_exp=re.Pattern, col_input=pd.DataFrame, col_output=pd.DataFrame, reg_exp_group=int):
    matched = reg_exp.search(data_row[col_input])
    if matched is None:
        return data_row[col_output]
    lookFor = matched.group(reg_exp_group)
    if lookFor.isalpha():
        return int(NUMS[lookFor.lower()])
    if lookFor is not None:
        return lookFor
    return data_row[col_output]


def inputCurrency(data_row=pd.DataFrame, reg_exp=re.Pattern, col_input=pd.DataFrame, col_output=pd.DataFrame, reg_exp_group=int):
    matched = reg_exp.search(data_row[col_input])
    if matched is None:
        return data_row[col_output]
    lookFor = matched.group(reg_exp_group)
    lookFor = lookFor.upper()
    if lookFor != "USD" or lookFor != "ARS":
        if lookFor == "U$S":
            lookFor = "USD"
        if lookFor == "U$D":
            lookFor = "USD"
        if lookFor == "DOLARES":
            lookFor = "USD"
        if lookFor == "PESOS":
            lookFor = "ARS"
        return lookFor
    if lookFor is not None:
        return lookFor
    return int(data_row[col_output])