print("INPUT DAN OUTPUT DI PYTHON".center(60, "/"))
"""
Kita akan belajar,
meminta masukan dari user, 
menyimpan nilai pada variabel,
dan mencetak nilai ke layar.
"""

# OUTPUT
print("OUTPUT".center(60, "~"))
"""
Menggunakan fungsi print() untuk langsung mengeluarkan sesuatu ke layar
"""
print("Langsung mengeluarkan ke layar".rjust(45, ">"))
print("Ini adalah output dengan menggunakan fungsi print()\n")

print("Memasukan nilai variabel ke string".rjust(45, ">"))
# langsung menggabungkan variabel dalam statement print()
print("langsung menggabungkan".ljust(45, "<"))
nilai_variabel = "Bulan"
print("Dia yang pergi, hilang."
      "\nMeninggalkan kenangan. Dengan harapan, akan pulang"
      "\nBernama", nilai_variabel, "\n")

# dengan menggunakan mekanisme string format
print("Mekanisme string format".ljust(45, "<"))
print("kapan pulang, {}".format(nilai_variabel))
print("""Dia yang {}, hilang.
meninggalkan {}. 
Dengan {}, akan pulang.
Bernama {}""".format("pergi",  # ini akan masuk ke dalam string
                     "kenangan",  # sesuai urutannya
                     "harapan",
                     nilai_variabel), "\n")

print("Operator % dan argument specifiers".ljust(45, "<"))
# dengan menggunakan operator % dan argument specifiers sesuai tipe datanya
# %d = Integers
# %s = string
# %f = float
# %.<digit>f = Float dengan sejumlah digit angka dibelakang koma
# %x/%X = bilangan bulat dengan representasi Hexa(huruf kecil/huruf besar)
nama = "Alfidza Tryana Maani"
kelas = 12
nilai = 9.5
list_teman = ["Sofia", "Intan", "Ipa"]
print("""Waktu itu, %s sudah menduduki bangku kelas %d.
Sama seperti saya. Ulangan bahasa inggrisnya 
mendapat nilai %.1f.""" % (nama, kelas, nilai))
# cocok jika nilai variabel yang mau dimasukkan ke dalam string itu banyak.

print("Kenapa nanti kelas %d, saya kenal %s" % (kelas, nama))
# argument specifiersnya harus berurutan sesuai dalam string
print("%s adalah sedikit dari banyak temannya." % list_teman, "\n")
# tipe data set, list otomatis di konversi ke str.
# tipe tuple, cuma bisa yang berisi 1 item. Jadi tidak efektif
# kalau argument specifiersnya cuma satu, tidak usah pakai kurung

print("contoh mencetak representasi hexa".ljust(45, "<"))
a, b = 10, 11
print("%d dan %d adalah nilainya" % (a, b))
print("a : %x dan b : %X adalah representasi Hexa-nya" % (a, b), "\n")


# INPUT
print("INPUT".center(60, "~"))
"""
Untuk mendapatkan input dari user, gunakan fungsi input().
Argumen dalam kurung adalah teks yang ingin ditampilkan, 
Input user akan tersimpan dalam variabel sebelum tanda '='
"""
print("FILL YOUR PROFILE".center(45, "="))
name = input("Name : ")
address = input("Address : ")
age = (input("Age : "))
school = input("School : ")
religion = input("Religion : ")
print("\n", "MY PROFILE".center(45, "="))
print("""Name : %s
Address : %s
Age : %s
School : %s
Religion : %s""" % (name, address, age, school, religion))

print("KUIS SEDERHANA".center(45, "="))
kali = int(input("4 * 5 = "))
print("kali = ", kali, "tipe", type(kali))
bagi = float(input("5 / 2 = "))
print("bagi = ", bagi, "tipe", type(bagi))
tambah = float(input("3.5 + 2 = "))
print("tambah = ", tambah, "tipe", type(tambah))
kurang = int(input("45 - 5 = "))
print("kurang = ", kurang, "tipe", type(kurang))
ekspresi = eval(input("operasi matematika = "))
# fungsi eval berfungsi menyelesaikan ekspresi matematika
print("hasilnya = ", ekspresi)
