import requests
import pandas as pd

crime_data_url = "https://api.stat.uz/api/v1.0/data/hududlar-kesimida-jami-royxatga-olingan-jinoyatla?lang=en&format=xlsx"
population_density_data_url = "https://api.stat.uz/api/v1.0/data/aholining-zichligi?lang=en&format=xlsx"
income_data_url = "https://api.stat.uz/api/v1.0/data/hududlar-boyicha-aholi-jon-boshiga-umumiy-darom?lang=en&format=xlsx"

def download_data(url, save_path):
    ## with ssl verification disabled, was not possible to download without this
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"File downloaded successfully and saved to: {save_path}")
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file from {url}. Error: {e}")
  
download_data(crime_data_url, "data/crime_data.xlsx")
download_data(population_density_data_url, "data/population_density_data.xlsx")
download_data(income_data_url, "data/income_data.xlsx")

##

def convert_and_extract_data(excel_file_path, sheet_name, start_row, end_row, start_col, end_col, csv_file_path):
    # Loading Excel file
    df_all = pd.read_excel(excel_file_path, sheet_name=sheet_name, skiprows=lambda x: x < start_row - 1)

    # Extracting rows and columns
    col_start, col_end = pd.Index(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + ['AA', 'AB']).get_loc(start_col), pd.Index(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + ['AA', 'AB']).get_loc(end_col)
    df_selected = df_all.iloc[:end_row - start_row + 1, col_start:col_end + 1]

    # Saving as a CSV file
    df_selected.to_csv(csv_file_path, index=False)

    print(f"Data from rows {start_row} to {end_row} and columns {start_col} to {end_col} saved to {csv_file_path}.")

# for crime data
excel_file_path = 'data/crime_data.xlsx'
sheet_name = 'Лист1'
start_row, end_row = 4, 20
start_col, end_col = 'D', 'S'
csv_file_path = 'data/crime_data.csv'

convert_and_extract_data(excel_file_path, sheet_name, start_row, end_row, start_col, end_col, csv_file_path)

# for demographic data
excel_file_path = 'data/population_density_data.xlsx'
sheet_name = 'UZB'
start_row, end_row = 4, 19
start_col, end_col = 'D', 'AB'
csv_file_path = 'data/population_density_data.csv'

convert_and_extract_data(excel_file_path, sheet_name, start_row, end_row, start_col, end_col, csv_file_path)

# for income data
excel_file_path = 'data/income_data.xlsx'
sheet_name = 'Лист2'
start_row, end_row = 4, 19
start_col, end_col = 'D', 'AA'
csv_file_path = 'data/income_data.csv'

convert_and_extract_data(excel_file_path, sheet_name, start_row, end_row, start_col, end_col, csv_file_path)

income_data = pd.read_csv('data/income_data.csv')
income_data = income_data.rename(columns={'Territories': 'Regions'})
income_data.to_csv('data/income_data.csv', index=False)