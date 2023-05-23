print("Learn Basic Python - 03 Type Data\n")
"""
Tipe data adalah jenis penyimpanan data 
dengan karakter tertentu. Sebelumnya, harus tau dulu dengan variabel
Variabel adalah sebuah tempat di memori komputer untuk menyimpan nilai
dengan tipe tertentu menggunakan operator assigment (=)
misal :
"""
print("PENGENALAN VARIABEL".center(45, "+"))
x = 2
print("x = 2, Artinya kita menyimpan", x, "ke dalam x menggunakan operator assigmemnt(=)")

# NUMBERS (numeric)
"""
Tipe numerik pada python dibagi menjadi 3
    1. INTEGER (int)
    2. FLOAT (float)
    3. COMPLEX
"""
    # INTEGER (int)
print("INTEGER".center(45,"*"))
"""Dibatasi oleh memori yang tersedia 
    bukan panjang tertentu. Sehingga tidak perlu 
    menggunakan variabel yang menampung big number, 
    cth: long long, biginteger, atau sejenisnya
    Run contoh dibawah, akan 'MemoryError'
"""
# x = [0]*9999999
# x[1] = 1

# for j in range(2, 9999999):
#    x[j] = x[j-1] + x[j-2]
# print(x[10000])
"""Sebagai bilangan bulat, 
    penulisannya tidak boleh ada titiknya 
    karena akan di deteksi sebagai tipe float.
    Contohnya, angka 1000.
"""
int = 1000
notint = 1.000
print(int, "bertipe", type(int))
print(notint, "bertipe", type(notint), "\n")

    # Float (float)
print("TIPE FLOAT".center(45,"*"))
"""Ditandai dengan titik di angkanya (decimal points)"""
type_float = 2.5
print(type_float, "bertipe", type(type_float))

"""Dibatasi digitnya pada 15 desimal yang dihitung
    setelah 2 digit dibelakang koma.
    bilangan ke 16-nya akan dipotong"""
digit_float = 0.1234567890123456189 #angka 7 dibulatkan jadi 8, angka 8, 9 dipotong secara otomatis
print(digit_float, "berjumlah", len(str(digit_float)), "\n")

    # Complex dan imajiner (complex)
print("TIPE COMPLEX".center(45, "*"))
"""Nilainya dituliskan dalam formulasi x + yj
    x adalah bilangan real
    y adalah bilangan imajiner.
    Sering digunakan oleh matematikawan"""
tipe_complex = 2 + 5j
print(tipe_complex, "bertipe", type(tipe_complex), "\n")

# STRINGS (str)
print("TIPE STRING".center(45, "*"))
"""
String adalah urutan dari karakter unicode.
Dideklarasikan dengan tanda petik (tunggal/ganda) diawal dan diakhir.
Jika lebih dari 1 baris, gunakan 3 tanda petik.
"""
tipe_str = "Simpang jalan di keningmu"
tipe_str_multiline = """Program Your Future
Develop Your self
Debugging Your plan"""
print(tipe_str, "bertipe", type(tipe_str))
print(tipe_str_multiline, "bertipe", type(tipe_str_multiline))

"""
Seperti list dan tuple, string bisa di slicing operator [], (operator pemotong elemen).
Tapi tidak bisa diubah karena elemen string bersifat immutable (tetap), 
Kalau string utuhnya bisa berubah karena bersifat mutable (bisa berubah).
format operator :
variabel[urutan elemen]
variabel[awal urutan elemen : akhir urutan elemen]
urutannya dimulai dari 0.
spasi tetap dihitung
"""
print(tipe_str[7], "inilah potongan elemen ke-7 (spasi)") # memotong elemen yang ke-7 (spasi)
print(tipe_str[0:7], "inilah potongan elemen dari 0 ke 7 \n") #memotong dari elemen ke-0 sampai ke-7

# BOOLEAN (bool)
print("TIPE BOOLEAN".center(45, "*"))
"""
Hanya ada 2 nilai, True & False.
Mewakili nilai kebenaran (truth values).
Truth values adalah nilai yang dapat diuji benar atau salah
Berikut objek bawaan yang didefinisikan bernilai salah
1. None dan False
2. Angka nol dari semua tipe numeric: 0, 0.0, 0j. Decimal(0), Fraction(0,1)
3. Urutan dan koleksi yang kosong, '', "", (), {}, set(), range(0)
Operasi dan fungsi bawaan yang memiliki hasi boolean akan selalu mengembalikan 
0 atau False untuk yang bernilai salah, dan 1 atau true untuk yang bernilai benar.
"""
tipe_bool = True
print(tipe_bool, "bertipe", type(tipe_bool))
print(4 == 4) # ini operasi yang mengembalikan nilai bool
print(bool(notint), "\n") # ini fungsi pengkonversi tipe lain ke boolean

# LIST
print("TIPE LIST".center(45, "*"))
"""
Adalah jenis kumpulan data terurut(ordered sequence).
Elemennya bisa dari tipe data yang berbeda.
Dideklarasikan dengan kurung siku, dan
elemennya dipisahkan dengan koma.
List juga bisa di slicing [] dengan indeks yang dimulai dari 0.
Elemennya bisa di ubah, ditambah
"""
tipe_list = [2, 25, 0.5, "ans", True, 3 + 5j]
print(tipe_list, "bertipe", type(tipe_list))
print(tipe_list[0], "ini adalah potongan elemen paling awal dengan index 0 dari list")
print(tipe_list[3], "potongan elemen dengan index ke-3")
print(tipe_list[-2], "potongan elemen dengan index paling belakang") # tanda mines artinya diurut dari belakan
print(tipe_list[2:4], "potongan elemen dari  index ke-2 sampai sebelum ke-4")
print(tipe_list[:4], "potongan elemen dari awal sampai sebelum index 4")
print(tipe_list[-3:], "potongan elemen dari index ke-3 dari belakang sampai paling belakang")
print(tipe_list[1:6:2], "potongan elemen dari index 1 sampai index 6 dengan step 2")
# dalam hal ini hanya index 1, 3, 5. step artinya sama seperti beda pada barisan aritmatika


tipe_list.append("tambahan")
tipe_list[0] = "2 jadi 10"
del tipe_list[3]
print(tipe_list, "setelah diubah, dihapus dan ditambahkan\n")

# TUPLE
print("TIPE TUPLE".center(45, "*"))
"""
Adalah jenis dari list yang tidak dapat diubah elemennya.
Umumnya digunakan untuk data yang bersifat sekali tulis dan 
dapat dieksekusi lebih cepat. Didefinisikan dengan kurung dan 
elemen yang dipisahkan dengan koma. Seperti list, TUPLE juga bisa di slicing, 
namun elemennya tidak dapat diubah.
"""
tipe_tuple = (12, "adalah", 4 + 2j, 5.8)
print(tipe_tuple, "bertipe", type(tipe_tuple))
print(tipe_tuple[0:3], "adalah elemen dari index ke-0 sampai ke-2")
# Kode ini akan TypeError: 'tuple' object does not support item assignment
# karena item tuple tidak bisa di ubah
# tipe_tuple[1] = "kamu"
print(tipe_tuple[1], "adalah elemen index ke-1\n")


# SET
print("TIPE SET".center(45,"*"))
"""
Set adalah kumpulan item unik tanpa urutan (unordered cellection).
Didefinisikan dengan kurawal dan elemennya dipisahkan dengan koma.
Tidak bisa melakukan slicing karena itemnya tidak terurut.
Bisa melakukan union : menyatukan data duplikat dengan menghapusnya langsung
Bisa melakukan intersection : mengurutkan dari kecil ke besar
"""
tipe_set = {1,1,5,5,1,2,"dua", "dua", 3,3,3}
print(tipe_set, "union xx dari {1,1,1,2,'dua', 'dua', 3,3,3}")
# print(tipe_set[2:5])
print(len(tipe_set), "\n")

# DICTONARY
print("TIPE DICTIONARY".center(45, "*"))
"""
Kumpulan pasangan kunci-nilai yang bersifat tidak berurutan.
Dapat didunakan untuk menyimpan data kecil maupun besar.
Didefinisikan dengan kurawal dan :
1. Setiap elemen pasangan kunci-nilai dipisahkan dengan koma
2. Kunci dan nilai dipisahkan dengan titik koma
3. Key dan value dapat berupa tipe variabel/objek apapun
Formatnya begini :
tipe_dict = {kunci : nilai, kunci : nilai, kunci : nilai}
Untuk mengakses datanya, kita harus mengetahui kuncinya (key)
"""
tipe_dict = {5 : "nilai", "kamu" : "aku"}
print("{1 : 'nilai', 'kunci' : 2} bertipe", type(tipe_dict))
print(tipe_dict[5])
print(tipe_dict['kamu'])
# print(tipe_dict[2]) #ini tidak akan mengeluarkan apa2 karena kuncinya salah


print("THANK YOU".center(45, "*"))