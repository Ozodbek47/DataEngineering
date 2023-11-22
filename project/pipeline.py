import requests

crime_data_url = "https://api.stat.uz/api/v1.0/data/hududlar-kesimida-jami-royxatga-olingan-jinoyatla?lang=en&format=xlsx"
demographic_data_url = "https://api.stat.uz/api/v1.0/data/aholining-zichligi?lang=en&format=xlsx"
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
download_data(demographic_data_url, "data/demographic_data.xlsx")
download_data(income_data_url, "data/income_data.xlsx")

### 