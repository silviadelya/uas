from view.input_nilai import*

data_mahasiswa = {}


def tambah_data():
    global data_mahasiswa
    print("TAMBAH DATA")
    print("------------")
    nama = nama_input()
    nim = nim_input()
    tugas = tugas_input()
    uts = uts_input()
    uas = uas_input()
    nilai_akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
    data_mahasiswa[nama] = [nim, tugas, uts, uas, nilai_akhir]
    print()
    return data_mahasiswa


def ubah_data():
    if len(data_mahasiswa) <= 0:
        no_data()
    else:
        print("UBAH DATA")
        print("-----------")
        nama = input("Nama Anda\t: ")
        if nama in data_mahasiswa.keys():
            nim = int(input("NIM Mahasiswa\t: "))
            tugas = int(input("Nilai Tugas\t: "))
            uts = int(input("Nilai UTS\t: "))
            uas = int(input("Nilai UAS\t: "))
            nilai_akhir = (tugas*30/100)+(uts*35/100)+(uas*35/100)
            data_mahasiswa[nama] = [nim, tugas, uts, uas, nilai_akhir]
            print()


def hapus_data():
    if len(data_mahasiswa) <= 0:
        no_data()
    else:
        print("HAPUS DATA")
        print("-----------")
        nama = input("Nama Anda\t: ")
        if nama in data_mahasiswa.keys():
            del data_mahasiswa[nama]
            print()


def cari_data():
    print("CARI DATA")
    print("---------")
    nama = input("Nama anda\t: ")
    print()
    for nama in data_mahasiswa.items():
        print(72*"=")
        print("|      Nama      |     NIM     | Tugas |  UTS  |  UAS  |     Akhir    |")
        print(72*"=")
        print(f"| {nama[1][0]:15} | {nama[0]:10} | {nama[1][1]:5} | {nama[1][2]:5} | {nama[1][3]:5} | {nama[1][4]:12} |")
        print(72*"=")
        print()


def no_data():
    print("DAFTAR NILAI")
    print("------------")
    print(72*"=")
    print("|      Nama      |     NIM     | Tugas |  UTS  |  UAS  |     Akhir    |")
    print(72*"=")
    print("|                             TIDAK ADA DATA                           |")
    print(72*"=")
    print()
