print("KONVERSI ANTAR TIPE DATA".center(45, "~"))
"""
Merubah tipe data ke tipe data lainnya.
Menggunakan fungsi konversi
Misal : int(), float(), str(), bool()
"""
# KONVERSI DARI INTEGER
"""
Dari int ke float, otomatis akan bertambah .0 di belakang nilainya
"""
print("KONVERSI DARI INTEGER".center(45, "+"))
data_int = 25
print(data_int, "masih bertipe", type(data_int))
data_str = str(data_int)
data_bool = bool(data_int)
data_float = float(data_int)
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_str), "menjadi", data_str, "\n")

# KONVERSI DARI FLOAT
"""
Konversi float ke int akan bersifat floor/truncating 
atau menghilangkan nilai di belakang koma.
"""
print("KONVERSI DARI FLOAT".center(45, "+"))
data_float = 7.8
print(data_float, "masih bertipe", type(data_float))
data_str = str(data_float)
data_bool = bool(data_float)
data_int = int(data_float)
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
print("Dikonversi ke", type(data_int), "menjadi", data_int)
print("Dikonversi ke", type(data_str), "menjadi", data_str, "\n")

# KONVERSI DARI STRING
print("KONVERSI DARI STRING".center(45, "+"))
"""
Konversi dari-dan-ke string akan melalui pengujian untuk dipastikan validitasnya
Tipe string hanya bisa di konversi ke float dan int, 
jika dan hanya jika karakternya adalah angka.
Kalau ada karakter lain maka error, termasuk string kosong.
Jika di konversi ke bool, akan False jika string kosong.
Jika di konvert ke list, set, tuple, maka akan mengikuti definisi mereka
"""
data_str = "25"
print(data_str, "masih bertipe", type(data_str))
data_bool = bool(data_str)
data_int = int(data_str)
data_float = float(data_str)
data_list = list(data_str)
data_set = set(data_str)
data_tuple = tuple(data_str)
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
print("Dikonversi ke", type(data_int), "menjadi", data_int)
print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_tuple), "menjadi", data_tuple)
print("Dikonversi ke", type(data_set), "menjadi", data_set)
print("Dikonversi ke", type(data_list), "menjadi", data_list, "\n")
# KOVERSI DARI BOOLEAN
print("KONVERSI DARI BOOLEAN".center(45, "+"))
data_bool = True
print(data_bool, "masih bertipe", type(data_bool))
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Dikonversi ke", type(data_int), "menjadi", data_int)
print("Dikonversi ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_float), "menjadi", data_float, "\n")

data_bool = False
print(data_bool, "masih bertipe", type(data_bool))
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Dikonversi ke", type(data_int), "menjadi", data_int)
print("Dikonversi ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_float), "menjadi", data_float, "\n")

# KONVERSI DARI LIST
print("KONVERSI DARI LIST".center(45, "+"))
data_list = [2, 5, 7.2, "Aku", "Kamu", "Dia"]
print(data_list, "masih bertipe", type(data_list))
data_str = str(data_list)
# data_int = int(data_list) Tidak bisa di convert
data_bool = bool(data_list)
# data_float = float(data_list) Tidak bisa di convert
data_tuple = tuple(data_list)
data_set = set(data_list)
# data_dict = dict(data_list) Tidak bisa diconvert, kecuali listnya terurut seperti dict
# print("Dikonversi ke", type(data_dict), "menjadi", data_dict, "\n")
# print("Dikonversi ke", type(data_int), "menjadi", data_int)
# print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
print("Dikonversi ke", type(data_tuple), "menjadi", data_tuple)
print("Dikonversi ke", type(data_set), "menjadi", data_set, "\n")

# KONVERSI DARI TUPLE
print("KONVERSI DARI TUPLE".center(45, "+"))
data_tuple = (4, 3, 1, "Aku")
print(data_tuple, "Masih bertipe", type(data_tuple))
data_str = tuple(data_tuple)
data_bool = bool(data_tuple)
# data_int = int(data_tuple) Tidak bisa diconvert
# data_float = float(data_tuple) Tidak bisa diconvert
data_list = list(data_tuple)
data_set = set(data_tuple)
# data_dict = dict(data_tuple) Tidak bisa diconvert
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
# print("Dikonversi ke", type(data_int), "menjadi", data_int)
# print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_set), "menjadi", data_set)
print("Dikonversi ke", type(data_list), "menjadi", data_list, "\n")
# print("Dikonversi ke", type(data_dict), "menjadi", data_dict, "\n")

# KONVERSI DARI SET
print("KONVERSI DARI SET".center(45, "+"))
data_set = {4, 3, 1, "Aku"}
print(data_set, "Masih bertipe", type(data_set))
data_str = str(data_set)
data_bool = bool(data_set)
# data_int = int(data_set)  Tidak bisa diconvert
# data_float = float(data_set) #Tidak bisa diconvert
data_list = list(data_set)
data_tuple = tuple(data_set)
# data_dict = dict(data_tuple) #Tidak bisa diconvert
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
# print("Dikonversi ke", type(data_int), "menjadi", data_int)
# print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_tuple), "menjadi", data_tuple)
print("Dikonversi ke", type(data_list), "menjadi", data_list, "\n")
# print("Dikonversi ke", type(data_dict), "menjadi", data_dict, "\n")

# KONVERSI DARI DICTIONARY
print("KONVERSI DARI DICTIONARY".center(45, "+"))
"""
Konversi dari dictionary ke set, tuple, list hanya mengambil kuncinya,
sedangkan valuenya tidak.
Kalau dikonversika ke string, mengambil semuanya, kunci, nilai, bahkan kurawalnya
"""
data_dict = {"aku":4, 2: "kamu"}
print(data_dict, "masih bertipe", type(data_dict))
data_bool = bool(data_dict)
# data_int = int(data_dict) Tidak bisa diconvert
# data_float = float(data_dict) float() argument must be a string or a number, not 'dict'
data_list = list(data_dict)
data_set = set(data_dict)
data_tuple = tuple(data_dict)
data_str = str(data_dict)
print("Dikonversikan ke", type(data_str), "menjadi", data_str)
print("Dikonversi ke", type(data_bool), "menjadi", data_bool)
# print("Dikonversi ke", type(data_int), "menjadi", data_int)
# print("Dikonversi ke", type(data_float), "menjadi", data_float)
print("Dikonversi ke", type(data_tuple), "menjadi", data_tuple)
print("Dikonversi ke", type(data_set), "menjadi", data_set)
print("Dikonversi ke", type(data_list), "menjadi", data_list, "\n")


print("THANKS".center(45, "+"))
