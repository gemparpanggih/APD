import time

bulan = ("Januari", "Februari", "Maret","April", "Mei", "Juni",
         "Juli", "Agustus", "September", "Oktober", "November", "Desember")

sekarang = time.time()
infowaktu = time.localtime(sekarang)

def welcome():
	print(' ')
	print('====================================')
	print('== Toko Buku Gramedia INFORMATIKA ==')
	print('====================================')
	time.sleep(1.5)
	menu()

def menu():
	print('\n=======================================================')
	print('[1]Pilih 1 untuk melihat daftar buku yang sedang diskon')
	print('[2]Pilih 2 untuk membeli buku')
	print('[3]Pilih 3 untuk melihat ketentuan diskon')
	print('[0]Pilih 0 untuk keluar dari aplikasi')
	print('=======================================================')

	
	pilih = input('Masukkan nomor pilihan yang anda inginkan : ')

	if pilih == '1':
		daftar_buku()
	elif pilih == '2':
		beli_buku()
	elif pilih == '3':
		ketentuan_diskon()
	elif pilih == '0':
		keluar()
	else:
		print('\nAngka yang anda masukkan tidak dikenal\nAnda kami kembalikan ke menu utama\n')
		time.sleep(1.5)
		menu()

def daftar_buku():
	print('\n================================================')
	print('!! Daftar Buku yang sedang diskon !!')
	print('1. The Wish of Dragon\t[Harga Normal: Rp.50000')
	print('2. Emperor Domination\t[Harga Normal: Rp.100000')
	print('3. Legend of Futian\t\t[Harga Normal: Rp.150000')
	print('4. Love Letter\t\t\t[Harga Normal: Rp.120000')
	print('5. Miracle in Cell No 7\t[Harga Normal: Rp.500000')
	print('==================================================')
	time.sleep(1.5)
	back_to_menu()

def ketentuan_diskon():
	print('\n================================================')
	print('!! Ketentuan Disekon Toko Buku Gramedia !!')
	print('1. Diskon buku akan berlaku sebanyak 15% jika membeli lebih dari atau sama dengan 1')
	print('2. Diskon buku akan berlaku sebanyak 25% jika membeli lebih dari 5 sampai dengan batas maksimal 10')
	print('3. Diskon buku akan berlaku sebanyak 50% jika membeli lebih dari 10')
	print('==================================================')
	time.sleep(1.5)
	back_to_menu()


def beli_buku():
	print('\nDaftar Buku Yang Sedang Diskon')
	print('1. The Wish of Dragon\t[Kode: twd]')
	print('2. Emperor Domination\t[Kode: edn]')
	print('3. Legend of Futian\t\t[Kode: lof]')
	print('4. Love Letter\t\t\t[Kode: lot]')
	print('5. Miracle in Cell No 7\t[Kode: mc7]\n')

	print('[1] Pilih No 1 jika ingin melanjutkan')
	print('[0] Pilih No 0 jika ingin kembali ke menu utama')

	pilih = input('Pilih salah satu angka jika anda ingin melanjutkan? : ')
	if pilih == '1': 
		time.sleep(1.5)
		hitung_harga()
	elif pilih == '0':
		time.sleep(1.5)
		hitung_harga()
	else:
		print('\nAngka yang anda masukkan tidak dikenal\nAnda kami kembalikan ke menu utama\n')
		time.sleep(1.5)
		menu()

def hitung_harga():
	nama = input('\nMasukkan Nama Pembeli\t : ')
	kode = input('Masukkan Kode Buku\t\t : ')

	if kode == 'twd':
		try:
			print('\nAnda Memilih Buku "The Wish of Dragon"')
			jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
			harga = 50000
			jwb = jb*harga
			if jb >= 1 and jb <= 5  : 
				disc = jwb * (15/100) #diskon 15% 
			elif jb > 5 and jb <=10 : 
				disc = jwb * (25/100) #diskon 25% 
			elif jb > 10 : 
				disc = jwb * (50/100) #diskon 50%
			else:
				print('\nMaaf jumlah yang dimasukkan tidak cocok')
				hitung_harga()
		except ValueError:
			print("\nHarap masukkan nominal yang benar!\n")
			hitung_harga()

		
	elif kode == 'edn':
		try:
			print('\nAnda Memilih Buku "Emperor Domination"')
			jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
			harga = 100000
			jwb = jb*harga
			if jb >= 1 and jb <= 5  : 
				disc = jwb * (15/100) #diskon 15%
			elif jb > 5 and jb <=10 : 
				disc = jwb * (25/100) #diskon 25% 
			elif jb > 10 : 
				disc = jwb * (50/100) #diskon 50%
			else:
				print('\nMaaf jumlah yang dimasukkan tidak cocok')
				hitung_harga()
		except ValueError:
			print("\nHarap masukkan nominal yang benar!\n")
			hitung_harga()
		
	elif kode == 'lof':
		try:
			print('\nAnda Memilih Buku "Legend of Futian"')
			jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
			harga = 150000
			jwb = jb*harga
			if jb >= 1 and jb <= 5  : 
				disc = jwb * (15/100) #diskon 15%
			elif jb > 5 and jb <=10 : 
				disc = jwb * (25/100) #diskon 25% 
			elif jb > 10 : 
				disc = jwb * (50/100) #diskon 50%
			else:
				print('\nMaaf jumlah yang dimasukkan tidak cocok')
				hitung_harga()
		except ValueError:
			print("\nHarap masukkan jumlah yang benar!\n")
			time.sleep(1.5)
			hitung_harga()

	elif kode == 'lot':
		try:
			print('\nAnda Memilih Buku "Love Letter"')
			jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
			harga = 120000
			jwb = jb*harga
			if jb >= 1 and jb <= 5  : 
				disc = jwb * (15/100) #diskon 15%
			elif jb > 5 and jb <=10 : 
				disc = jwb * (25/100) #diskon 25% 
			elif jb > 10 : 
				disc = jwb * (50/100) #diskon 50%
			else:
				print('\nMaaf jumlah yang dimasukkan tidak cocok')
				hitung_harga()
		except ValueError:
			print("\nHarap masukkan jumlah yang benar!\n")
			time.sleep(1.5)
			hitung_harga()

	elif kode == 'mc7':
		try:
			print('\nAnda Memilih Buku "Miracle in Cell No 7"')
			jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
			harga = 500000
			jwb = jb*harga
			if jb >= 1 and jb <= 5  : 
				disc = jwb * (15/100) #diskon 15%
			elif jb > 5 and jb <=10 : 
				disc = jwb * (25/100) #diskon 25% 
			elif jb > 10 : 
				disc = jwb * (50/100) #diskon 50%
			else:
				print('\nMaaf jumlah yang dimasukkan tidak cocok')
				hitung_harga()
		except ValueError:
			print("\nHarap masukkan jumlah yang benar!\n")
			time.sleep(1.5)
			hitung_harga()
		
	else:
		print('\nMaaf kode yang dimasukkan tidak cocok, silahkan masukkan ulang!\n')
		time.sleep(1.5)
		hitung_harga()

	ht = jwb - disc

	print("\n=======================================")
	print("               Kwitansi               ")
	print("=======================================")
	print("Nama Pembeli, ",nama)
	print("Waktu Pembelian", infowaktu[2], bulan[infowaktu[1]-1], infowaktu[0])
	print("Harga Total Sebelum Diskon\t : Rp. ",jwb)
	print("Potongan Harga           \t : Rp. ",disc)
	print("Harga Yang Harus Di Bayar\t : Rp. ",ht)
	print(" ")
	print("=======================================")
	print("           Terima Kasih           \n")

	exit = input('Apakah anda ingin kembali ke menu utama? (y/n) : ')
	if exit == 'y':
		welcome()
	elif exit == 'n':
		keluar()
	else:
		keluar()

def back_to_menu():
	pilih = input('Apakah anda ingin kembali ke menu utama? (y/n) : ')
	if pilih == 'y':
		time.sleep(1.5)
		menu() 
	elif pilih == 'n':
		print('Anda memilih menutup aplikasi')
		keluar()
	else:
		print('Anda memasukkan nilai yang salah! Harap inputkan kembali')
		time.sleep(1.5)
		back_to_menu()

def keluar():
	exit()


if __name__ == '__main__':
    while True:
    	welcome()

