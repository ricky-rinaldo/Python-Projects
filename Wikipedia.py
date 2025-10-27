import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL target
url = "https://www.wikipedia.org/"

# Mengambil konten halaman
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Memeriksa apakah request berhasil

    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari tabel dengan selector yang diberikan
    table = soup.select_one(
        '#mw-content-text > div.mw-content-ltr.mw-parser-output > table.wikitable.sortable.sticky-header.jquery-tablesorter')

    if table:
        # Mengubah tabel HTML menjadi DataFrame pandas
        df = pd.read_html(str(table))[0]

        # Menyimpan ke file Excel
        excel_file = "wikipedia.xlsx"
        df.to_excel(excel_file, index=False)

        print(f"Data berhasil disimpan ke {excel_file}")
        print(f"Jumlah data: {len(df)} baris")
    else:
        print("Tabel tidak ditemukan dengan selector tersebut.")

except requests.exceptions.RequestException as e:
    print(f"Error saat melakukan request: {e}")
except Exception as e:
    print(f"Terjadi error: {e}")