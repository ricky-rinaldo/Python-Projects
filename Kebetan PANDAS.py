import pandas as pd

# Membuat dictionary data
data = {
    'Nama': ['Ricky', 'Sari', 'Rayyan', 'Athalla'],
    'Usia': [44, 37, 10, 7],
    'Kota': ['Jakarta', 'Cimahi', 'Cimahi', 'Cimahi'],
    'Pekerjaan': ['Wiraswasta', 'Wiraswasta', 'Pelajar', 'Pelajar']
}

# Membuat DataFrame dari dictionary
df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)

# Menyimpan DataFrame ke dalam file CSV tanpa index
df.to_csv("data.csv", index=False, encoding="utf-8-sig")

# Membaca ulang file data.csv
dt_baru = pd.read_csv('data.csv')

# Menampilkan DataFrame (ulang)
print(dt_baru)

# Menyimpan dengan pemisah titik koma (;)
df.to_csv("data.csv", index=False, sep=";")

# Menyimpan dengan encoding utf-8-sig (supaya bisa dibuka di Excel tanpa masalah karakter)
df.to_csv("data.csv", index=False, encoding="utf-8-sig")

# Menyimpan hanya kolom tertentu
df.to_csv("data.csv", index=False, columns=["Nama", "Usia"])

# Menambahkan header khusus
df.to_csv("data.csv", index=False, header=["Nama Lengkap", "Umur", "Kota Asal"])

# Gunakan perintah ini untuk mengecek lokasi file
import os
print(os.getcwd())  # Menampilkan lokasi penyimpanan skrip dan file CSV

# Menampilkan 5 data pertama
print(df.head())
# Menampilkan 10 data pertama
print(df.head(10))

print(df.info())
print(df.tail())
print(df.describe())
