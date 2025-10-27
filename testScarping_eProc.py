import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook

# URL target scraping
url = "https://eprocurement.pupuk-indonesia.com/beranda"

# Headers untuk menyamar sebagai browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Mengirim request ke website
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Memeriksa apakah request berhasil

    # Parsing konten HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari semua elemen dengan selector CSS yang diberikan
    # Selector pertama untuk judul/nama perusahaan
    company_names = soup.select(
        '#root > div:nth-child(1) > div > div.profile-content > div > div.tab-pane.fade.show.active > div > div > div > div.panel-body.undefined > center > div > div:nth-child(1) > table:nth-child(1) > thead > tr > td > h4')

    # Selector kedua untuk detail informasi (alamat, email, dll)
    company_details = soup.select(
        '#root > div:nth-child(1) > div > div.profile-content > div > div.tab-pane.fade.show.active > div > div > div > div.panel-body.undefined > center > div > div:nth-child(1) > table:nth-child(1) > thead > tr > td > h4')

    # Jika selector tidak ditemukan, coba selector alternatif
    if not company_names:
        company_names = soup.find_all('h4', class_=None)  # Mencari semua tag h4

    if not company_details:
        company_details = soup.find_all('td', class_=None)  # Mencari semua tag td

    # Menyiapkan list untuk menyimpan data
    data = []

    # Mengambil teks dari elemen yang ditemukan
    names = [name.get_text(strip=True) for name in company_names]
    details = [detail.get_text(strip=True) for detail in company_details]

    # Membuat dictionary untuk data
    # Asumsi: nama perusahaan berada di index genap, detail di index ganjil
    for i in range(min(len(names), len(details))):
        data.append({
            'Nama Perusahaan': names[i] if i < len(names) else '',
            'Detail': details[i] if i < len(details) else ''
        })

    # Membuat DataFrame dari data yang dikumpulkan
    df = pd.DataFrame(data)

    # Menyimpan ke file Excel
    excel_filename = "Scraping eproc pupuk.xlsx"
    df.to_excel(excel_filename, index=False)

    print(f"Data berhasil disimpan ke {excel_filename}")

except requests.exceptions.RequestException as e:
    print(f"Error saat melakukan request: {e}")
except Exception as e:
    print(f"Terjadi error: {e}")