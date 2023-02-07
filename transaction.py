import os
import quit
import random
import datetime


def transactionLanding():
    print("""======SELAMAT DATANG DI APLIKASI FROZEN FOOD======
    PILIHLAH MENU
    1. Order Pesanan
    2. Order to wishlist
    3. Deskripsi Frozen Food
    4. Keluar dari aplikasi
    """)
    chooseMenu = int(input())
    if chooseMenu == 1:
        transactionOrder()
    elif chooseMenu == 2:
        wishlist()
    elif chooseMenu == 3:
        description()
    elif chooseMenu == 4:
        quit.textQuit()
    else:
        os.system("cls")
        print("HARUS PILIH 1-4 !!!")
        transactionLanding()

totalInput = 0
thingsShop = []
totalShop = []
priceShop = []
a = 0
b = 0

def transactionOrder():
    while True:
        global totalInput,thingsShop,totalShop,priceShop,a,b
        print("""        ========== MENU FROZEN FOOD ==========
    --------------------------------------
    | KODE | JENIS FROZEN FOOD |  HARGA |
    --------------------------------------
    |   1  | TEMPURA    |  Rp. 20000,00 |
    |   2  | SOSIS      |  Rp. 18000,00 |
    |   3  | CHIKUWA    |  Rp. 22000,00 |
    |   4  | FISH ROLL  |  Rp. 16000,00 |
    |   5  | CRAB STICK |  Rp. 25000,00 |
    |   6  | SCALLOP    |  Rp. 23500,00 |
    |   7  | BAKSO      |  Rp. 14000,00 |
    |   8  | NUGGET     |  Rp. 19500,00 |
    |   9  | KATSU      |  Rp. 40000,00 |
    |   10 | DIMSUM     |  Rp. 25000,00 |
    """)
        pembelian_barang = str(input("Kode Barang : "))
        if pembelian_barang == "1":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang1 = 20000
            hargaBarang1 *= jmlh_beli_barang
            thingsShop.append("TEMPURA  ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang1)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "2":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_2 = 18000
            hargaBarang_2 *= jmlh_beli_barang
            thingsShop.append("SOSIS    ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_2)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "3":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_3 = 22000
            hargaBarang_3 *= jmlh_beli_barang
            thingsShop.append("CHIKUWA  ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_3)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "4":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_4 = 16000
            hargaBarang_4 *= jmlh_beli_barang
            thingsShop.append("FISHROLL ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_4)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "5":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_5 = 25000
            hargaBarang_5 *= jmlh_beli_barang
            thingsShop.append("CRABSTICK")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_5)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "6":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_6 = 23500
            hargaBarang_6 *= jmlh_beli_barang
            thingsShop.append("SCALLOP  ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_6)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "7":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_7 = 14000
            hargaBarang_7 *= jmlh_beli_barang
            thingsShop.append("BAKSO    ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_7)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "8":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_8 = 19500
            hargaBarang_8 *= jmlh_beli_barang
            thingsShop.append("NUGGET   ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_8)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "9":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_9 = 40000
            hargaBarang_9 *= jmlh_beli_barang
            thingsShop.append("KATSU    ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_9)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        elif pembelian_barang == "10":
            totalInput += 1
            jmlh_beli_barang = int(input("Total Barang : "))
            os.system("cls")
            hargaBarang_10 = 25000
            hargaBarang_10 *= jmlh_beli_barang
            thingsShop.append("DIMSUM   ")
            totalShop.append(jmlh_beli_barang)
            priceShop.append(hargaBarang_10)
            input_ulang = str(input( "Apakah anda ingin menambah barang lagi?(YES/NO)"))
            if str.upper(input_ulang) == "YES":
                pass
            elif str.upper(input_ulang) == "NO":
                break
            if input_ulang == "NO":
                break
        else:
            print("Mohon maaf, barang tidak ditemukan")
    print("==============MY FROZEN FOOD=============")
    print("=========================================")
    print("Nama Barang | Jumlah | Total Harga |")
    print("---------------------------------------")
    jumlah_print = 0
    total_harga = sum(priceShop)
    while totalInput > jumlah_print:
        jumlah_print += 1
        print(thingsShop[a],"  |   ", totalShop[a] , "  |  ", priceShop[a], "     ")
        a += 1
    print("=======================================")
    print("Total Pembelian       | ", total_harga, " |")
    print("""
    1.Transfer Bank
    2.Cash on Delivery
    3.Kartu kredit
    4.Alfamaret/Indomaret
    """)
    while True:
        buyMethod = int(input("Pilih Metode Pembayaran -> "))
        os.system("cls")
        now = datetime.datetime.now()
        if buyMethod == 1:
            name = str(input("Masukkan Nama Anda: "))
            address = str(input("Masukkan Alamat Anda: "))
            os.system("cls")
            print(f"""
            Virtual Account   : {random.getrandbits(20)}
            Total Harga       : Rp{total_harga}
            Pembeli           : {name}
            Tanggal Pembelian : {now.strftime("%y-%m-%d %H:%M:%S")}
            Alamat Pengiriman : {address}
            """)
            break
        elif buyMethod == 2:
            name = str(input("Masukkan Nama Anda: "))
            address = str(input("Masukkan Alamat Anda: "))
            os.system("cls")
            print("Anda dikenakan biaya penanganan sejumlah Rp2.500")
            print(f"""
            Total Harga       : Rp{total_harga + 2500}
            Pembeli           : {name}
            Tanggal Pembelian : {now.strftime("%y-%m-%d %H:%M:%S")}
            Alamat Pengiriman : {address}
            Estimasi sampai -> 2 hari dari pemesanan
            """)
            break
        elif buyMethod == 3:
            name = str(input("Masukkan Nama Anda: "))
            address = str(input("Masukkan Alamat Anda: "))
            os.system("cls")
            print("Anda dikenakan biaya penanganan sejumlah Rp1.000")
            print(f"""
            Rekening Tujuan   : {random.getrandbits(25)}
            Total Harga       : Rp{total_harga + 1000}
            Pembeli           : {name}
            Tanggal Pembelian : {now.strftime("%y-%m-%d %H:%M:%S")}
            Alamat Pengiriman : {address}
            """)
            break
        elif buyMethod == 4:
            name = str(input("Masukkan Nama Anda: "))
            address = str(input("Masukkan Alamat Anda: "))
            os.system("cls")
            print("Datanglah ke Alfamart/Indomaret terdekat dan berikan nomor virtual account yang tertera di bawah ini")
            print("Anda dikenakan biaya penanganan sebesar Rp1.500")
            print(f"""
            Virtual Account   : {random.getrandbits(30)}
            Total Harga       : Rp{total_harga + 1500}
            Pembeli           : {name}
            Tanggal Pembelian : {now.strftime("%y-%m-%d %H:%M:%S")}
            Alamat Pengiriman : {address}
            Batas pembayaran -> 12 jam setelah pemesanan
            """)
            break
        else:
            print("Harus Pilih 1-4!!!")
            pass

item = []
price = []
totalPrice = 0

def wishlist():
    os.system("cls")
    global item,price,totalPrice
    while True:
        print("""        ========== MENU FROZEN FOOD ==========
        --------------------------------------
        | KODE | JENIS FROZEN FOOD |  HARGA |
        --------------------------------------
        |   1  | TEMPURA    |  Rp. 20000,00 |
        |   2  | SOSIS      |  Rp. 18000,00 |
        |   3  | CHIKUWA    |  Rp. 22000,00 |
        |   4  | FISH ROLL  |  Rp. 16000,00 |
        |   5  | CRAB STICK |  Rp. 25000,00 |
        |   6  | SCALLOP    |  Rp. 23500,00 |
        |   7  | BAKSO      |  Rp. 14000,00 |
        |   8  | NUGGET     |  Rp. 19500,00 |
        |   9  | KATSU      |  Rp. 40000,00 |
        |   10 | DIMSUM     |  Rp. 25000,00 |
        """)
        inputCode = int(input("Masukkan kode barang : "))
        if inputCode == 1:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("TEMPURA")
            price.append(totalItem*20000)
            totalPrice += totalItem*20000
        elif inputCode == 2:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("SOSIS")
            price.append(totalItem*18000)
            totalPrice += totalItem*18000
        elif inputCode == 3:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("CHIKUWA")
            price.append(totalItem*22000)
            totalPrice += totalItem*22000
        elif inputCode == 4:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("FISH ROLL")
            price.append(totalItem*16000)
            totalPrice += totalItem*16000
        elif inputCode == 5:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("CRAB STICK")
            price.append(totalItem*25000)
            totalPrice += totalItem*25000
        elif inputCode == 6:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("SCALLOP")
            price.append(totalItem*23500)
            totalPrice += totalItem*23500
        elif inputCode == 7:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("BAKSO")
            price.append(totalItem*14000)
            totalPrice += totalItem*14000
        elif inputCode == 8:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("NUGGET")
            price.append(totalItem*19500)
            totalPrice += totalItem*19500
        elif inputCode == 9:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("KATSU")
            price.append(totalItem*40000)
            totalPrice += totalItem*40000
        elif inputCode == 10:
            totalItem = int(input("Masukkan jumlah barang : "))
            os.system("cls")
            item.append("DIMSUM")
            price.append(totalItem*25000)
            totalPrice += totalItem*25000
        else:
            print("Barang Tidak Terdaftar")
        otherBuy = str(input("Apakah ingin menambah wishlist(YES/NO)?"))
        os.system("cls")
        if otherBuy == "NO":
            if len(item) == 0:
                quit.textQuit()
                break
            else:
                fakturWishlist()
                quit.textQuit()
                break
        elif otherBuy == "YES":
            wishlist()
            break
        else:
            otherBuy = str(input("Apakah ingin menambah wishlist(YES/NO)?"))
            os.system("cls")
            if otherBuy == "NO":
                if len(item) == 0:
                    quit.textQuit()
                    break
                else:
                    fakturWishlist()
                    quit.textQuit()
                    break
def fakturWishlist():
    global item,price,totalPrice
    print(f"""
    Berikut adalah wishlist frozen food Anda
    --------------------------------
    | Barang      = {item}         
    | Harga       = {price}        
    | Total Harga = Rp {totalPrice} 
    --------------------------------
    Bersemangatlah dalam menabung untuk membeli wishlist frozen food kamu 🔥😁
    """)

def description():
    print("""
    1. TEMPURA    = Makanan laut yang dicelup ke dalam adonan berupa tepung terigu dan kuning telur
    2. SOSIS      = Jenis produk daging yang biasanya dibuat dari daging giling bersama dengan garam, rempah-rempah, dan perasa lainnya.
    3. CHIKUWA    = Bahan makanan Jepang berupa olahan daging ikan berbentuk seperti tabung. 
    4. FISH ROLL  = Olahan ragam menu ikan yang pembuatannya mudah. Bahan baku pembuatan Fish Roll adalah ikan.
    5. CRAB STICK = Jenis makanan laut yang terbuat dari pati dan ikan putih yang dihaluskan. 
    6. SCALLOP    = Scallop adalah olahan frozen food dari ikan.
    7. BAKSO      = Dibuat dari campuran daging sapi giling dan tepung tapioka.
    8. NUGGET     = Produk makanan yang terdiri dari sepotong kecil daging ayam tanpa tulang yang dilapisi tepung roti.
    9. KATSU      = Ayam goreng Jepang yang dibuat dengan remah roti panko.
    10.DIMSUM     = Makanan berisi daging dan sayuran ini populer di dunia dari Hong Kong.
    """)
    backOrder=str(input("Apakah Anda ingin order(YES/NO)?"))
    if backOrder == "YES":
        transactionOrder()
    else:
        os.system("cls")
        quit.textQuit()
