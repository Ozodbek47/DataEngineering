import zipfile
import urllib.request
import pandas as pd
import sqlite3

direct_download_link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
zip_file_path = "mowesta-dataset.zip"
csv_file_name = "data.csv"

# Downloading and unzipping the data
urllib.request.urlretrieve(direct_download_link, zip_file_path)

with zipfile.ZipFile(zip_file_path, 'r') as z_ref:
    z_ref.extract(csv_file_name, '.')

# Reshaping the data
df = pd.read_csv(csv_file_name, sep=';', decimal=',', usecols=range(11), names=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Latitude (WGS84)","Longitude (WGS84)","Verschleierung (m)","Aufenthaltsdauer im Freien (ms)", "Batterietemperatur in °C", "Geraet aktiv"], header=0)
df.to_csv('data/data0.csv')

selected_columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]
df = df[selected_columns]
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

# Transforming the data
df[["Temperatur", "Batterietemperatur"]] = df[["Temperatur", "Batterietemperatur"]].apply(lambda x: (x * 9/5) + 32)

# Validating the data
df = df[df["Geraet"] > 0]
df = df[df["Monat"] <= 12]

# SQLite
sqlite_types = {"Geraet": "BIGINT", "Hersteller": "TEXT", "Model": "TEXT", "Monat": "BIGINT", "Temperatur": "FLOAT", "Batterietemperatur": "FLOAT", "Geraet aktiv": "TEXT"}
db_path = "temperatures.sqlite"
table_name = "temperatures"

with sqlite3.connect(db_path) as conn:
    df.to_sql(table_name, conn, index=False, if_exists='replace', dtype=sqlite_types)
