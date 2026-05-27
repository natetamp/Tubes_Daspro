# File : Tugas_2572005.py
# Program Sistem Manajemen Laundry

def login(user, pw):
    username=["admin", "kasir", "owner"]
    password=[123,321,111]
    auth=False
    for i in range (0, len(username),1):
        if user==username[i] and pw==password[i]:
            user=username[i]
            auth=True
    if auth==True:
        print("Login Berhasil")
        print()
        if user=="admin":
            menu_admin()
        elif user=="kasir":
            menu_kasir()
        elif user=="owner":
            menu_owner()
    else:
        print ("Login Gagal")
    return 

def menu_admin ():
    while True:
        print("Welcome, admin!")
        print("            ===MENU===            ")
        A=["Update Status", "Hapus Data", "Lihat Semua Data", "Logout"]
        for i in range (0, len(A),1):
            print(f"{i+1}. {A[i]}")
        choice=int(input("Pilih menu (1-4): "))
        if choice==1:
            stat_update()
        elif choice==2:
            hapus_data()
        elif choice==3:
            lihat_data("admin")
        elif choice==4:
            logout()
            break
        else:
            print("Menu tidak tersedia")
    return choice
def menu_kasir ():
    while True:
        print("Welcome, kasir!")
        print("            ===MENU===            ")
        A=["Tambah Data Laundry", "Lihat Data Laundry", "Cetak Struk", "Logout"]
        for i in range (0, len(A),1):
            print(f"{i+1}. {A[i]}")
        choice=int(input("Pilih menu (1-4): "))
        if choice==1:
            tambah_data()
        elif choice==2:
            lihat_data("kasir")
        elif choice==3:
            cetak_struk()
        elif choice==4:
            logout()
            break
        else:
            print("Menu tidak tersedia")
    return choice

def menu_owner ():
    print("Welcome, owner!")
    while True:
        print("            ===MENU===            ")
        A=["Total Pendapatan", "Jumlah Transaksi", "Logout"]
        for i in range (0, len(A),1):
            print(f"{i+1}. {A[i]}")
        choice=int(input("Pilih menu (1-3): "))
        if choice==1:
            pendapatan()
        elif choice==2:
            jumlah_transaksi()
        elif choice==3:
            logout()
            break
        else:
            print("Menu tidak tersedia")
    return choice

def stat_update():
    return

def hapus_data():
    return

def lihat_data():
    return

def tambah_data():
    while True:
        global nama, berat, layanan
        print("===Input Laundry===")
        pelanggan=int(input("Jumlah Pelanggan: "))
        for i in range (0,pelanggan,1):
            nama[i]=str(input("Nama  : "))
            berat[i]=float(input("Berat  : "))
            layanan[i]=str(input("Layanan  : "))
        
    return

def cetak_struk():
    return

def pendapatan():
    return

def jumlah_transaksi():
    return

def logout():
    return


def main ():
    print ("             NGORTIS LAUNDRY")
    print("            ===LOGIN PAGE===           ")
    username = str(input("Masukkan username: "))
    password = int(input("Masukkan password: "))
    login(username, password)

if __name__=='__main__':
    invoice=[]
    nama=[]
    layanan=[]
    berat=[]
    harga=[]
    status=[]
    main()
