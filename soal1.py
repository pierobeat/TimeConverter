#kekurangan program, blum bisa melakukan kondisi jika input < 35999
import math     #memanfaatkan modul .floor() pada library math

def timeConverter(data):   
    jam = math.floor(data / 3600)       #memakai math.floor utk menerima hasil data (inputan kita) dibagi 3600
    menit = math.floor(data / 60) % 60  #memakai math.floor utk menerima hasil data (inputan kita) dibagi 3600
    detik = data % 3600                 #membangun variabel detik dengan data (inputan) modulo 3600
    detik %= 60                         #nilai dari kalkulasi sebelum modulo 60
    return "%d:%02d:%02d" % (jam, menit, detik) #menyimpan nilai jam, menit, detik dengan format pada tulisan sebelumnya

while True:             #membuat perulangan while, selama inputan bukan integer
        try:
            n = int(input('masukkan angka : ')) #input data
            print(timeConverter(n))             #mengeluarkan hasil function
            break                               #memberhentikan perulangan
        except ValueError:                      
            print("invalid input!")             #mengeluarkan print ini ketika inputan tidak sesuai