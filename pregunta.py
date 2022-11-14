"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_general(row):
    row = row.lower()
    row = row.replace("-", " ")
    row = row.replace("_", " ")
    row = row.strip()

    return row

def clean_barrio(row):
    row = row.lower()
    row = row.strip()
    row = row.replace("-", " ")
    row = row.replace("_", " ")
    row = row.replace(".", " ")
    row = row.replace(" ", "")

    return row

def clean_date(row):
    row_split = row.split("/")
    if len(row_split[0]) <= 2:
        row_split[0], row_split[-1] = row_split[-1], row_split[0]

    return "/".join(row_split)

def clean_monto_credito(row):
    row = row.replace("$", "")
    row = row.replace(".00", "")
    row = row.replace(",", "")
    #row = row.replace(" ", "")

    return row

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df = df.drop_duplicates()
    df = df.dropna()

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(lambda x: str(x).lower())
    df['sexo'] = df['sexo'].apply(lambda x: x.lower())
    df['idea_negocio'] = df['idea_negocio'].apply(clean_general)
    df['barrio'] = df['barrio'].apply(clean_barrio)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(clean_date)
    df['monto_del_credito'] = df['monto_del_credito'].apply(clean_monto_credito)
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    df["línea_credito"] = df["línea_credito"].apply(clean_general)
    df = df.drop_duplicates()
    df['barrio'] = df['barrio'].apply(clean_barrio)

    return df
