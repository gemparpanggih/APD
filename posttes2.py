import time

bulan = ("Januari", "Februari", "Maret","April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember")#tipe data Array

sekarang = time.time()
infowaktu = time.localtime(sekarang)

print(' ')
print('===================== Mebel Kayu Barokah =====================')
print(' ')
print(' 	Menjuual Balok Kayu dengan Harga Terbaik')
print(' ')

print('===============================================================')
print('Daftar Harga Balok Kayu')
print('1. Balok Kayu Ukuran Besar, Harga Normal Rp. 5000')
print('2. Balok Kayu Ukuran Sedang, Harga Normal Rp. 10000')
print('3. Balok Kayu Ukuran Kecil, Harga Normal Rp. 15000')
print('\nADA DISKON NYA JUGA LO\n')
print('!! PROGRAM INI DIBUAT OLEH GEMPAR PANGGIH DWI PUTRA !!')
print('!! NIM 2009106022 FROM INFORMATIKA A 2020 !!')
print('===============================================================')
print(' ')

print('===============================================================')
print(' Menentukan Luas, Volume, dan Keliling Balok yang Ingin Dibeli ')
print('===============================================================')
print(' ')

name = str(input("Masukkan Nama Pembeli\t = "))#tipe data string, VARIABLE INPUT PERTAMA
usia = int(input("Masukkan Usia Pembeli\t = "))#tipe data interger, VARIABLE INPUT KEDUA
alamat = str(input("Masukkan Alamat Pembeli\t = "))#VARIABLE INPUT KETIGA
p = int(input("Masukkan Panjang Kayu\t = "))#tipe data interger, VARIABLE INPUT KEEMPAR
l = int(input("Masukkan Lebar Kayu\t\t = "))#tipe data interger, VARIABLE INPUT KELIMA
t = int(input("Masukkan Tinggi Tinggi\t = "))#tipe data interger, VARIABLE INPUT KEENAM

lbalok = 2*((p*l)+(p*t)+(l*t))
vbalok = (p*l*t)
kbalok = 4*(p*l*t)

print('\n===============================================================')

print('Jadi balok dengan ukuran Panjang {} cm, Lebar {} cm, dan Tinggi {} cm'. format(p,l,t))
print('Mempunyai Luas: {} cm, Volume: {} cm, dan Keliling: {} cm'. format(lbalok,vbalok,kbalok))

if lbalok >= 500 :
	print('\nAnda Memilih Balok Kayu Ukuran Besar')
	jk = int(input('\nJumlah Balok Kayu Ukuran Besar yang Ingin Di Beli\t : '))	#tipe data Interger, VARIABLE INPUT KETUJUH
	harga = 10000
	jumlah = jk*harga
	if jk <= 100 : disc = 0
	elif jk > 100 and jk <=200 : disc = 0.50*100*harga #diskon 25%, tipe data float
	elif jk > 200 : disc = 1.50*100*harga #diskon 50%, tipe data float 
	
elif lbalok >=100 :
	print('\nAnda Memilih Balok Kayu Ukuran Sedang')
	jk = int(input('\nJumlah Balok Kayu Ukuran Sedang yang Ingin Di Beli\t : ')) #tipe data Interger, VARIABLE INPUT KEDELAPAN	
	harga = 5000
	jumlah = jk*harga
	if jk <= 100 : disc = 0
	elif jk > 100 and jk <=200 : disc = 0.50*100*harga #diskon 25%, tipe data float 
	elif jk > 200 : disc = 1.50*100*harga #diskon 50%, tipe data float

else:
	print('\nAnda Memilih Balok Kayu Ukuran Kecil')
	jk = int(input('\nJumlah Balok Kayu Ukuran Sedang yang Ingin Di Beli\t : ')) #tipe data Interger, VARIABLE INPUT KESEMBILAN
	harga = 1000
	jumlah = jk*harga
	if jk <= 100 : disc = 0
	elif jk > 100 and jk <=200 : disc = 0.50*100*harga #diskon 25%, tipe data foat 
	elif jk > 200 : disc = 1.50*100*harga #diskon 50%, tipe data float

harga = jumlah - disc

print("\n==================================")
print("             Kwitansi             ")
print("==================================")
print("Atas Nama",name)
print("Usia:",usia,"Tahun")
print("Dengan Alamat,",alamat)
print("Tanggal", infowaktu[2], bulan[infowaktu[1]-1], infowaktu[0])
print("Harga Total Sebelum Diskon\t : Rp. ",jumlah)
print("Potongan Harga           \t : Rp. ",disc)
print("Harga Yang Harus Di Bayar\t : Rp. ",harga)
print("==================================")
print(" ")
print("==================================")
print("           Terima Kasih           ")
print("==================================\n")

print("!!BONUS!!List Varible yang Di Pakai")
listt =["name","usia","alamat","p","l","t","jk"]
print(listt[0])
print(listt[1])
print(listt[2])  
print(listt[3])
print(listt[4])
print(listt[5])
print(listt[6])
