# STYLE GUIDE IN PYTHON CODE
print("STYLE GUIDE IN PYTHON")

"""
Guido, pembuat bahasa Python, merasakan bahwa kode lebih sering dibaca
dibandingkan ditulis sehingga panduan ini lebih ditekankan untuk 
memudahkan membaca kode dan membuatnya  selalu konsisten 
pada (hampir) setiap proyek Python yang ada.
Eitss, jangan salah. 
Pada kasus-kasus tertentu, keputusan untuk memodifikasi tetap ada pada
penulis kodenya. Sometime, sebuah kode dapat terbaca lebih jelas
walaupun tidak mengikuti satu atau lebih panduan ini.
But, pada umumnya inilah style guide-nya...
"""

# INDENTASI
"""
Gunakan 4 spasi sebagai indentasi untuk menulis kode bertingkat. 
Statement yang memiliki indentasi yang sama dan diletakkan secara
berurutan dianggap sebagai blok satement. Contohnya gini...
"""
variabel_pertama = 5
variabel_kedua = variabel_pertama + 5
if variabel_kedua >= 5:
    variabel_pertama *= 2
    print(variabel_pertama + variabel_kedua)

# BARIS LANJUTAN
"""
Seringkali, saat menulis kode, kode tidak cukup dituliskan dalam satu baris sehingga harus menggunakan baris lanjutan. Umumnya, bisa menggunakan tanda hubung, kurung, kurawal, atau hanging indent seperti yang disarankan pada PEP-008. Supaya lebih paham, swipe left deh...
"""
# foo = long_function_name(var_one, var_two,
#                        var_three, var_four)