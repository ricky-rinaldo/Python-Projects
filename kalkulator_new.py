while True:

    print ('\nprogram kalkulator')
    print ('1. perjumlahan')
    print ('2. pengurangan')
    print ('3. perkalian')
    print ('4. pembagian')

    pilihan = input("masukan pilihan = ")
    if pilihan not in ['1','2','3','4']:
        print('pilihan tidak tersedia. diulang lagi')
        continue

    a = float(input('masukan angka A = '))
    b = float(input('masukan angka B = '))

    if pilihan == "4" and b == 0:
        print ("Error : B tidak boleh 0")
        continue

    if pilihan == "1":
        hasil = a + b
        operasi = "+"

    elif pilihan == "2":
        hasil = a - b
        operasi = "-"

    elif pilihan == "3":
        hasil = a * b
        operasi = "x"

    elif pilihan == "4":
        hasil = a / b
        operasi = "/"

    print (f"Hasil {a} {operasi} {b} adalah {hasil}")

    ulang = input('apakah ingin mengulang : ')
    if ulang.lower() == 'n':
        break
print ('program selesai')

