import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


# Fungsi untuk mendapatkan semua kategori
def get_categories(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Mencari elemen kategori
    categories_section = soup.select_one('div.side_categories > ul > li > ul')
    categories = []

    for li in categories_section.find_all('li'):
        category_name = li.a.text.strip()
        category_url = urljoin(base_url, li.a['href'])
        categories.append((category_name, category_url))

    return categories


# Fungsi untuk mendapatkan detail buku dari sebuah halaman kategori
def get_books_from_category(category_url):
    books = []
    while True:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil semua buku di halaman ini
        for book in soup.select('article.product_pod'):
            title = book.h3.a['title']
            price = book.select_one('p.price_color').text
            availability = book.select_one('p.instock').text.strip()

            # Menentukan rating berdasarkan kelas
            rating_classes = book.select_one('p.star-rating')['class']
            rating_map = {
                'One': '1/5',
                'Two': '2/5',
                'Three': '3/5',
                'Four': '4/5',
                'Five': '5/5'
            }
            rating = rating_map.get(rating_classes[1], 'Tidak ada rating')

            books.append({
                'Judul': title,
                'Harga': price,
                'Ketersediaan': availability,
                'Rating': rating
            })

        # Cek apakah ada halaman berikutnya
        next_button = soup.select_one('li.next > a')
        if next_button:
            category_url = urljoin(category_url, next_button['href'])
        else:
            break

    return books


# URL dasar
base_url = 'https://books.toscrape.com/'

# Mendapatkan semua kategori
print("Mengambil daftar kategori...")
categories = get_categories(base_url)
print(f"Ditemukan {len(categories)} kategori")

# Membuat DataFrame untuk semua buku
all_books = pd.DataFrame()

# Loop melalui setiap kategori dan ambil bukunya
for category_name, category_url in categories:
    print(f"Mengambil buku dari kategori: {category_name}...")
    books = get_books_from_category(category_url)

    # Menambahkan kategori ke data buku
    for book in books:
        book['Kategori'] = category_name

    # Menambahkan ke DataFrame utama
    df = pd.DataFrame(books)
    all_books = pd.concat([all_books, df], ignore_index=True)

# Menyimpan ke file Excel
output_file = "testscraping.xlsx"
print(f"Menyimpan data ke {output_file}...")
all_books.to_excel(output_file, index=False, sheet_name='Data Buku')

print("Selesai! Data telah disimpan ke testscraping.xlsx")