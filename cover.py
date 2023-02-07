import os
import login
import quit

def coverLanding():
    os.system("cls")
    print("============================================")
    print("SELAMAT DATANG DI APLIKASI MY FROZEN FOOD")
    print("============================================")

def startApps():
    start = input("Ketik S untuk Start atau K untuk Keluar Aplikasi -> ")
    if start == "S":
        os.system("cls")
        print("Silahkan login terlebih dahulu\n")
        login.loginLanding()
    elif start == "K":
        print("Anda keluar dari aplikasi")
        quit.textQuit()
    else:
        os.system("cls")
        print("Harus Pilih S atau K !!!")
        startApps()
