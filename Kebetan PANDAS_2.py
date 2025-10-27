import pandas as pd
data = {
    'Nama': ['Ricky', 'Sari', 'Rayyan', 'Athalla'],
    'Usia': [44, 37, 10, 7],
    'Kota': ['Jakarta', 'Cimahi', 'Cimahi', 'Cimahi'],
    'Pekerjaan': ['Wiraswasta', 'Wiraswasta', 'Pelajar', 'Pelajar']
}
df = pd.DataFrame(data)

df.loc[df['Usia'] > 9, 'Pekerjaan'] = 'Mahasiswa' # merubah value ke Mahasiswa dari Pelajar

df['Gaji'] = [8000000, 8000000, 0,0] # Menambah key 'Gaji' dan value-nya

df.to_csv('data.csv') # mengupdate ke file data.csv

data_baru = pd.read_csv('data.csv') # membaca file data.csv yang telah di update

print(data_baru)

