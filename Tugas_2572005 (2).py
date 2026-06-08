# File : Tugas_2572005.py
# Program Sistem Manajemen Laundry

def login(user, pw):
    username = ["admin", "kasir", "owner"]
    password = [123, 321, 111]
    auth = False
    for i in range(0, len(username), 1):
        if user == username[i] and pw == password[i]:
            user = username[i]
            auth = True
    if auth == True:
        print("Login Berhasil")
        print()
        if user == "admin":
            menu_admin()
        elif user == "kasir":
            menu_kasir()
        elif user == "owner":
            menu_owner()
    else:
        print("Login Gagal")
    return auth


def menu_admin():
    while True:
        print("Welcome, admin!")
        print("            ===MENU===            ")
        A = ["Update Status", "Hapus Data", "Lihat Semua Data", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-4): "))
        if choice == 1:
            stat_update()
        elif choice == 2:
            hapus_data()
        elif choice == 3:
            lihat_data("admin")
        elif choice == 4:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice


def menu_kasir():
    while True:
        print("Welcome, kasir!")
        print("            ===MENU===            ")
        A = ["Tambah Data Laundry", "Lihat Data Laundry", "Cetak Struk", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-4): "))
        if choice == 1:
            tambah_data()
        elif choice == 2:
            lihat_data("kasir")
        elif choice == 3:
            cetak_struk()
        elif choice == 4:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice


def menu_owner():
    print("Welcome, owner!")
    while True:
        print("            ===MENU===            ")
        A = ["Total Pendapatan", "Jumlah Transaksi", "Logout"]
        for i in range(0, len(A), 1):
            print(f"{i+1}. {A[i]}")
        choice = int(input("Pilih menu (1-3): "))
        if choice == 1:
            pendapatan()
        elif choice == 2:
            jumlah_transaksi()
        elif choice == 3:
            lanjut_login()
            break
        else:
            print("Menu tidak tersedia")
    return choice


def hitung_harga(berat, layanan):
    if layanan == "Reguler":
        tarif = 5000
    else:  # Express
        tarif = 10000
    return berat * tarif


def stat_update():
    global nama, status, invoice
    # Cari data yang sudah terisi
    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Update Status Laundry===")
    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Status':<15}")
    print("-" * 55)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(status[i]):<15}")

    try:
        no = int(input("\nMasukkan nomor urut data yang ingin diupdate: ")) - 1
        if no < 0 or no >= len(nama) or nama[no] is None:
            print("Data tidak ditemukan.")
            return

        print("Pilih status baru:")
        print("1. Proses")
        print("2. Selesai")
        print("3. Diambil")
        pilih = int(input("Pilih (1-3): "))
        if pilih == 1:
            status[no] = "Proses"
        elif pilih == 2:
            status[no] = "Selesai"
        elif pilih == 3:
            status[no] = "Diambil"
        else:
            print("Pilihan tidak valid.")
            return
        print(f"Status {nama[no]} berhasil diupdate menjadi {status[no]}.")
    except (ValueError, IndexError):
        print("Input tidak valid.")
    return


def hapus_data():
    global nama, berat, layanan, harga, status, invoice
    # Cari data yang sudah terisi
    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Hapus Data Laundry===")
    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Status':<15}")
    print("-" * 55)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(status[i]):<15}")

    try:
        no = int(input("\nMasukkan nomor urut data yang ingin dihapus: ")) - 1
        if no < 0 or no >= len(nama) or nama[no] is None:
            print("Data tidak ditemukan.")
            return

        konfirmasi = input(f"Yakin ingin menghapus data atas nama {nama[no]}? (y/n): ")
        if konfirmasi.lower() == 'y':
            nama[no] = None
            berat[no] = None
            layanan[no] = None
            harga[no] = None
            status[no] = None
            invoice[no] = None
            print("Data berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    except (ValueError, IndexError):
        print("Input tidak valid.")
    return


def lihat_data(role):
    global nama, berat, layanan, harga, status, invoice

    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Data Laundry===")
    if role == "admin":
        print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Berat':>8} {'Layanan':<12} {'Harga':>12} {'Status':<12}")
        print("-" * 85)
        for i in range(len(nama)):
            if nama[i] is not None:
                print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(berat[i]):>7}kg {layanan[i]:<12} Rp{harga[i]:>10,.0f} {str(status[i]):<12}")
    else:  # kasir
        print(f"{'No':<5} {'Invoice':<12} {'Nama':<20} {'Berat':>8} {'Layanan':<12} {'Harga':>12}")
        print("-" * 75)
        for i in range(len(nama)):
            if nama[i] is not None:
                print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20} {str(berat[i]):>7}kg {layanan[i]:<12} Rp{harga[i]:>10,.0f}")
    print()
    return


def tambah_data():
    global nama, berat, layanan, harga, status, invoice

    # Cari indeks kosong pertama
    def cari_indeks_kosong():
        for i in range(len(nama)):
            if nama[i] is None:
                return i
        return -1

    # Cari nomor invoice terakhir
    def nomor_invoice_baru():
        nomor = 1
        for i in range(len(invoice)):
            if invoice[i] is not None:
                nomor = invoice[i] + 1
        return nomor

    while True:
        print("===Pilihan Layanan===")
        print("   1. Reguler   ")
        print("   2. Express   ")
        print("===Input Laundry===")
        try:
            pelanggan = int(input("Jumlah Pelanggan: "))
            if pelanggan <= 0:
                print("Jumlah pelanggan harus lebih dari 0.")
                continue
        except ValueError:
            print("Input tidak valid.")
            continue

        for i in range(0, pelanggan, 1):
            idx = cari_indeks_kosong()
            if idx == -1:
                print("Data penuh, tidak bisa menambah data baru.")
                return

            nama[idx] = str(input("Nama  : "))
            while True:
                try:
                    berat[idx] = float(input("Berat (kg): "))
                    if berat[idx] <= 0:
                        print("Berat harus lebih dari 0.")
                        continue
                    break
                except ValueError:
                    print("Input tidak valid.")

            while True:
                try:
                    pilih = int(input("Pilih layanan (1/2): "))
                    if pilih == 1:
                        layanan[idx] = "Reguler"
                        break
                    elif pilih == 2:
                        layanan[idx] = "Express"
                        break
                    else:
                        print("Layanan tidak valid")
                except ValueError:
                    print("Input tidak valid.")

            harga[idx] = hitung_harga(berat[idx], layanan[idx])
            status[idx] = "Proses"
            invoice[idx] = nomor_invoice_baru()

        print("Data berhasil dimasukkan")
        break
    return nama, berat, layanan


def cetak_struk():
    global nama, berat, layanan, harga, status, invoice

    data_ada = False
    for i in range(len(nama)):
        if nama[i] is not None:
            data_ada = True
            break

    if not data_ada:
        print("Belum ada data laundry.")
        return

    print("\n===Cetak Struk===")
    print("Masukkan nomor invoice yang ingin dicetak struknya.")

    # Tampilkan daftar invoice
    print(f"{'No':<5} {'Invoice':<12} {'Nama':<20}")
    print("-" * 40)
    for i in range(len(nama)):
        if nama[i] is not None:
            print(f"{i+1:<5} {str(invoice[i]):<12} {nama[i]:<20}")

    try:
        no_inv = int(input("\nNomor Invoice: "))
        idx = -1
        for i in range(len(invoice)):
            if invoice[i] == no_inv:
                idx = i
                break

        if idx == -1:
            print("Invoice tidak ditemukan.")
            return

        print()
        print("=" * 40)
        print("         NGORTIS LAUNDRY          ")
        print("=" * 40)
        print(f"Invoice  : {invoice[idx]}")
        print(f"Nama     : {nama[idx]}")
        print(f"Berat    : {berat[idx]} kg")
        print(f"Layanan  : {layanan[idx]}")
        print(f"Status   : {status[idx]}")
        print("-" * 40)
        print(f"Total    : Rp {harga[idx]:,.0f}")
        print("=" * 40)
        print("      Terima kasih sudah percaya   ")
        print("        kepada Ngortis Laundry!     ")
        print("=" * 40)
        print()
    except ValueError:
        print("Input tidak valid.")
    return


def pendapatan():
    global harga, status

    total = 0
    for i in range(len(harga)):
        if harga[i] is not None:
            total += harga[i]

    print("\n===Total Pendapatan===")
    print(f"Total Pendapatan (semua transaksi): Rp {total:,.0f}")
    print()
    return


def jumlah_transaksi():
    global nama

    jumlah = 0
    for i in range(len(nama)):
        if nama[i] is not None:
            jumlah += 1

    print("\n===Jumlah Transaksi===")
    print(f"Total Transaksi: {jumlah} transaksi")
    print()
    return


def logout():
    print("Logout berhasil, apakah ingin melanjutkan? (yes/1 untuk login kembali)")
    pilih = input("Pilihan: ").strip().lower()
    if pilih == "yes" or pilih == "1":
        return True
    else:
        print("Terima kasih telah menggunakan Ngortis Laundry. Sampai jumpa!")
        return False


def main():
    while True:
        print("             NGORTIS LAUNDRY")
        print("            ===LOGIN PAGE===           ")
        username = str(input("Masukkan username: "))
        password = int(input("Masukkan password: "))
        if login(username, password):
            break


def lanjut_login():
    if logout():
        main()


if __name__ == '__main__':
    invoice = 1000 * [None]
    nama = 1000 * [None]
    layanan = 1000 * [None]
    berat = 1000 * [None]
    harga = 1000 * [None]
    status = 1000 * [None]
    main()
