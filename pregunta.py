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
    #row = row.strip()
    row = row.replace("-", " ")
    row = row.replace("_", " ")
    #row = row.replace(".", " ")
    #row = row.replace(" ", "")

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
    row = row.replace(" ", "")

    return row

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)

    df = df.drop_duplicates()
    df = df.dropna()

    df['sexo'] = df['sexo'].apply(lambda x: x.lower())
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(lambda x: str(x).lower())
    df['idea_negocio'] = df['idea_negocio'].apply(clean_general)
    df['barrio'] = df['barrio'].apply(clean_barrio)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(float)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(clean_date)
    df['monto_del_credito'] = df['monto_del_credito'].apply(clean_monto_credito)
    df['monto_del_credito'] = df['monto_del_credito'].astype(int)
    df["línea_credito"] = df["línea_credito"].apply(clean_general)
    df = df.drop_duplicates()
    #df['barrio'] = df['barrio'].apply(clean_barrio)

    return df


""" A = [
        990,
        483,
        423,
        383,
        376,
        372,
        361,
        348,
        328,
        308,
        270,
        255,
        255,
        247,
        234,
        232,
        231,
        202,
        174,
        170,
        169,
        124,
        117,
        115,
        114,
        90,
        89,
        89,
        86,
        85,
        78,
        72,
        70,
        67,
        65,
        59,
        55,
        52,
        50,
        49,
        48,
        48,
        48,
        47,
        45,
        44,
        43,
        43,
        43,
        40,
        38,
        37,
        36,
        36,
        34,
        34,
        33,
        33,
        32,
        30,
        27,
        27,
        27,
        26,
        26,
        25,
        25,
        24,
        24,
        24,
        24,
        23,
        21,
        21,
        21,
        20,
        20,
        20,
        20,
        17,
        17,
        17,
        16,
        14,
        14,
        14,
        14,
        13,
        13,
        12,
        11,
        11,
        11,
        11,
        10,
        10,
        10,
        9,
        9,
        9,
        9,
        8,
        8,
        8,
        8,
        8,
        8,
        7,
        7,
        7,
        7,
        7,
        7,
        7,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        6,
        5,
        5,
        5,
        5,
        5,
        5,
        4,
        4,
        4,
        4,
        4,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        3,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]

B = clean_data()['barrio'].value_counts()
for i in range(len(B)):
    if A[i] != B[i]:
        print(f"{i}, test: {A[i]}, Mio: {B[i]}") """