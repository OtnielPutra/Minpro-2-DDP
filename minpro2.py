akun = {
    "otnil": "stecu"
}

lapanganleh = {"lapangan tersedia": ["bultang1", "bultang2", "bultang3"],
                "lapangan dipesan": []
}

print("nama = Otniel Putra Wardana")
print("NIM  = 2509116081")
print("minpro 2 reservasi lapangan bulu tangkis")

def login():
    while True:
        print("\n=== SELAMAT DATANG, PILIH OPSI UNTUK LOGIN KE APLIKASI RESERVASI LAPANGAN KAMI ===")
        print("\n1. Login Sebagai Admin")
        print("2. Login Sebagai Member")
        print("3. Keluar dari aplikasi")
        pilihan = input("pilihlah sesuai angka: ")
        if pilihan == "1":
            login_admin()
        elif pilihan == "2":
            login_member()
            break
        elif pilihan == "3":
            keluar_dari_aplikasi()
            break

def login_admin():
    while True:
        try:
            user = input("\nmasukan username: ")
            pw = input("masukan password: ")
        except KeyboardInterrupt:
            print("\njangan menekan kombinasi tombol")
        else:
            if user in akun and akun[user] == pw:
                print("login sukses, selamat datang", user)
                halaman_admin()
                break
            else:
                print("\nusername atau password yang anda masukan salah. Coba lagi")

def halaman_admin():
    while True:
        try:
            print("\n=== Selamat datang Atmin, Apa yang ingin anda lakukan? ===")
            print("1. menambahkan list lapangan bulu tangkis")
            print("2. list lapangan yang ada untuk sekarang")
            print("3. mengubah list lapangan")
            print("4. menghapus lapangan dari list lapangan")
            print("5. Keluar dan balik ke menu awal")
            pilihan = int(input("\npilih diantara 1-5 sesuai dengan kebutuhan: "))
        except ValueError:
            print("\nmasukan hanya angka saja")
        else:
            if pilihan == 1:
                tambah_list_lapangan()
            elif pilihan == 2:
                list_lapangan_sekarang()
            elif pilihan == 3:
                ubah_list_lapangan()
            elif pilihan == 4:
                hapus_list_lapangan()
            elif pilihan == 5:
                kevin = input("apakah anda ingin keluar? (y/n): ")
                if kevin == "y":
                    keluar_dari_aplikasi()
                    break
                elif kevin == "n":
                    halaman_admin()
            else:
                print("pilihan salah we")

#Create
def tambah_list_lapangan():
    try:
        lele_dumbo = input("Masukan nama lapangan: ")
    except KeyboardInterrupt:
        print("\njangan menekan kombinasi keybaord leh")
    else:
        lapanganleh["lapangan tersedia"].append(lele_dumbo)
        print(f"Lapangan {lele_dumbo} berhasil ditambahkan!")

#Read
def list_lapangan_sekarang():
    print("\n",lapanganleh["lapangan tersedia"])

#Update
def ubah_list_lapangan():
    try:
        print("Daftar lapangan sekarang:", lapanganleh["lapangan tersedia"])
        nama_lama = input("Masukkan nama lapangan yang ingin diubah: ")
    except KeyboardInterrupt:
        print("\njaga keyboardnya")
    else:
        if nama_lama in lapanganleh["lapangan tersedia"]:
            nama_baru = input("Masukkan nama lapangan baru: ")
            index = lapanganleh["lapangan tersedia"].index(nama_lama)
            lapanganleh["lapangan tersedia"][index] = nama_baru
            print(f"Lapangan '{nama_lama}' berhasil diubah menjadi '{nama_baru}'")
        else:
            print("Lapangan tidak ditemukan!")

#Delete
def hapus_list_lapangan():
    print("Daftar lapangan sekarng", lapanganleh["lapangan tersedia"])
    ingin_hapus = input("masukan nama lapangan yang ingin dihapus: ")
    if ingin_hapus in lapanganleh["lapangan tersedia"]:
        lapanganleh["lapangan tersedia"].remove(ingin_hapus)
        print("lapangan berhasil dihapus")
    else:
        print("lapangan tidak ditemukan")

def login_member():
    while True:
        try:
            mawi = input("\nhai member, silahkan masukan nama anda: ")
        except KeyboardInterrupt :
            print("\njangan ditekan kombinasi tombol semabrangan ya")
        else:
            print("selamat datang", mawi)
            menu_member(mawi)
            break
        return

def menu_member(memberbang):
    while True:
        try:
            print(f"\n=== APA YANG MAU KAU LAKUKAN", memberbang, "===")
            print("\n1. reservasi lapangan")
            print("2. membatalkan reservasi")
            print("3. keluar dari menu")
            mentok_honor = int(input("masukan angka sesuai yang anda mau: "))
        except ValueError:
            print("\nangka saja bang")
        except KeyboardInterrupt:
            print("\njangan menekan kombinasi we")
        else:
            if mentok_honor == 1:
                reservasi_lapangan()
            elif mentok_honor == 2:
                batal_reservasi()
            elif mentok_honor == 3:
                banh = input("apakah anda ingin keluar dari menu? (y/n): " )
                if banh == "y":
                    login()
                    break
                elif banh == "n":
                    menu_member()
            else:
                print("pilihan tidak valid!")

def reservasi_lapangan():
    print("\nLapangan tersedia:", lapanganleh["lapangan tersedia"])
    pilih = input("Masukan nama lapangan yang ingin anda pesan: ")
    if pilih in lapanganleh["lapangan tersedia"]:
        lapanganleh["lapangan tersedia"].remove(pilih)
        lapanganleh["lapangan dipesan"].append(pilih)
        print(f"Reservasi berhasil! Anda memesan {pilih}")
    else:
        print("Lapangan tidak tersedia atau sudah dipesan.")

def batal_reservasi():
    print("\nLapangan yang sedang dipesan:", lapanganleh["lapangan dipesan"])
    pilih = input("Masukan nama lapangan yang ingin dibatalkan: ")
    if pilih in lapanganleh["lapangan dipesan"]:
        lapanganleh["lapangan dipesan"].remove(pilih)
        lapanganleh["lapangan tersedia"].append(pilih)
        print(f"Reservasi {pilih} berhasil dibatalkan.")
    else:
        print("Lapangan itu belum anda pesan atau tidak ada di daftar.")

def keluar_dari_aplikasi():
    print("terima kasih telah menggunakan layanan kami")

login()