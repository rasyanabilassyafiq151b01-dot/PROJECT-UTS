db = []

print("""
                    ==============================
                            SELAMAT DATANG
                       PILIH ROLE ANDA DIBAWAH!
                    ==============================
                
                     1.Penjual          2.Pembeli
""")

role = input("Masukan Role Anda Disini:").lower()

while True:
    if role == "penjual":
        account = input("Apa Anda Sudah Mempunyai akun [YES/NO]:")
        if account == "YES":
            usn = input("Masukan Username:")
            pw = int(input("Masukan Password:"))
        elif account == "NO":
            n = input("Apa Anda Ingin Daftar Menjadi Penjual [YES/NO]:")
            if n == "YES":
                usn = input("Masukan Username Yang Anda Mau:") 
                pw  = int(input("Masukan Password Yang Anda Mau:"))

                user_account = [usn, pw]
                db.append(user_account)
                print("Selamat Anda Sudah Menjadi Penjual!!!")
            




