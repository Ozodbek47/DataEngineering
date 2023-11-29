import pandas as pd
import sqlalchemy as sql

if __name__ == '__main__':
    db_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    db_name = 'trainstops'
    table_name = 'trainstops'

    df = pd.read_csv(db_url, delimiter=';').drop(columns='Status', errors='ignore')

    if df is not None:
        df.dropna(subset=df.columns.to_list(), inplace=True)
        df = df.loc[df['Verkehr'].isin(["FV", "RV", "nur DPN"])]
        df = df.loc[df['IFOPT'].str.match(r'^.{2}:\d+:\d+(?::\d+)?$').fillna(False)]

        df['Laenge'] = pd.to_numeric(df['Laenge'].str.replace(',', '.'), errors='coerce')
        df['Breite'] = pd.to_numeric(df['Breite'].str.replace(',', '.'), errors='coerce')

        df = df[df['Laenge'].between(-90, 90) & df['Breite'].between(-90, 90)]

        database_connection = sql.create_engine(f"sqlite:///{db_name}.sqlite", echo=False)

        datatype_converter = {
            'NAME': sql.types.TEXT,
            'Verkehr': sql.types.TEXT,
            'IFOPT': sql.types.TEXT,
            'Laenge': sql.types.FLOAT,
            'Breite': sql.types.FLOAT,
            'DS100': sql.types.TEXT,
            'Betreiber_Name': sql.types.TEXT,
            'Betreiber_Nr': sql.types.BIGINT,
            'EVA_NR': sql.types.BIGINT,
        }

        df.to_sql(table_name, con=database_connection, if_exists="replace", index=False, dtype=datatype_converter)
