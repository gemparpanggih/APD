import os
import time

bulan = ("Januari", "Februari", "Maret","April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember")#tipe data Array

sekarang = time.time()
infowaktu = time.localtime(sekarang)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
	clear_screen()
	print(' ')
	print('===================== Toko Kue Abang Sule =====================\n')
	print('Menjual Kue dengan tekstur lembur dan tentunya nikmat\n')
	print('===============================================================')
	print(' ')
	time.sleep(2)
	daftar_kue()

def daftar_kue():
	print('')
	print("[1] Kue Keju Rp. 6000")
	print("[2] Kue Coklat Rp. 3500\n")

	kue = str(input("Silahkah pilih Nomor Kue yang anda inginkan = "))

	if kue == '1' :
		print('\nAnda Memilih Kue Keju')
		jumlahkue = int(input('\nJumlah Kue Keju yang Ingin Di Beli\t : '))	
		harga = 6000
		jumlah = jumlahkue*harga
		if jumlahkue == 0:
			print("Maaf jumlah kue yang di inputkan tidak valid, harap isi ulang\n")
			daftar_kue()
		elif jumlahkue <= 1 and jumlahkue < 4 : 
			diskon = 0
		elif jumlahkue >= 4  and jumlahkue <= 15 : 
			diskon = jumlah * (10/100) 
			print("Anda mendapat diskon 10%")
		elif jumlahkue >= 16 and jumlahkue <= 25: 
			diskon = jumlah * (15/100)
			print("Anda mendapat diskon 15%")
		elif jumlahkue > 25:
			print("Maaf jumlah kue yang di inputkan tidak valid, harap isi ulang\n")
			daftar_kue()
		
	elif kue == '2' :
		print('\nAnda Memilih Kue Coklat')
		jumlahkue = int(input('\nJumlah Kue Coklat yang Ingin Di Beli\t : ')) 
		harga = 3500
		jumlah = jumlahkue*harga
		if jumlahkue == 0:
			print("Maaf jumlah kue yang di inputkan tidak valid, harap isi ulang\n")
			daftar_kue()
		elif jumlahkue <= 1 and jumlahkue < 5 : 
			diskon = 0
		elif jumlahkue >= 5 and jumlahkue <= 20 : 
			diskon = jumlah * (7/100)
			print("Anda mendapat diskon 7%")
		elif jumlahkue >= 21 and jumlahkue <= 35 : 
			diskon = jumlah * (12/100)
			print("Anda mendapat diskon 12%") 
		elif jumlahkue > 35:
			print("Maaf jumlah kue yang di inputkan tidak valid, harap isi ulang\n")
			daftar_kue()

	jumlahharga = jumlah - diskon

	print("\n==================================")
	print("             Kwitansi             ")
	print("==================================")
	if kue=='1':
		print("Anda Membeli Kue Keju Sebanyak\t\t :",jumlahkue)
	elif kue=='2':
		print("Anda Membeli Kue Coklat Sebanyak\t : ",jumlahkue)
	print("Tanggal", infowaktu[2], bulan[infowaktu[1]-1], infowaktu[0])
	print("Harga Total Sebelum Diskon\t\t\t : Rp. ",jumlah)
	print("Potongan Harga\t\t\t\t\t\t : Rp. ",diskon)
	print("Harga Yang Harus Di Bayar\t\t\t : Rp. ",jumlahharga)
	print("==================================")
	print(" ")
	print("==================================")
	print("           Terima Kasih           ")
	print("==================================\n")

if __name__ == "__main__":
    while True:
        welcome()


