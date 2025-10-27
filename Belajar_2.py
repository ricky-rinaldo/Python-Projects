import csv
from bs4 import BeautifulSoup

# Buka file books.html
with open('books.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Ambil judul dan harga buku
judul_buku = [buku.a.text for buku in soup.find_all('h3')]
harga_buku = [harga.text.encode('latin-1').decode('utf-8') for harga in soup.find_all('p', class_='price_color')]

# Simpan ke CSV
with open('buku.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Judul Buku', 'Harga'])
    writer.writerows(zip(judul_buku, harga_buku))

print("Data berhasil disimpan ke buku.csv")
