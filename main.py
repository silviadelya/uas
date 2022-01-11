from view.view_nilai import *
from model.daftar_nilai import *


while True:
    print("Pilih Menu")
    print("----------")
    print("\n1.Tambah Data \n2.Ubah Data \n3.Hapus Data \n4.Cari Data \n5.Lihat Data \n6.Keluar")
    tanya = int(input("Masukkan pilihan\t: "))
    print()

    if tanya == 1:
        tambah_data()

    elif tanya == 2:
        ubah_data()

    elif tanya == 3:
        hapus_data()

    elif tanya == 4:
        cari_data()

    elif tanya == 5:
        cetak_daftar_nilai()

    elif tanya == 6:
        print("Program Selesai - Terima kasih!")
        break
