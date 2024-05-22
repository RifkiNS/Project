import datetime as dt
class data:

    __nama_lintasan = "Semarang"
    nama = ""
    tanggal = ""
    tempat = ""

    def __init__(self,Input_nama):
        self.nama = Input_nama
        self.tanggal = dt.date.today()
        self.tempat = "ITERA"
    def get_nama_lintasan(self):
        print("Nama Lintasan\t:",self.__nama_lintasan)


y = data("Rifki")

print(f"Nama \t\t: {y.nama}\nTanggal\t\t: {y.tanggal}\nTempat \t\t: {y.tempat}")
y.get_nama_lintasan()

TWT = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
kec_gel_p = [2250, 2250, 2250, 2000, 2000, 2000, 2000, 2000, 2250, 2250, 2250, 2250, 2250]
densitas = [2, 2, 2, 1.95, 1.95, 1.95, 1.95, 1.95, 2, 2, 2, 2, 2]

#Z = kec_gel_p[0] * densitas[0]
#print("impedansi \t:",Z)
impedensi = []
for i in range(len(TWT)):
    Z = kec_gel_p[i] * densitas[i]
    impedensi.append(Z)
    print("Impedensi ke-",i,":",Z)
print(impedensi)

r = []    
for i in range(1,len(impedensi)):
    R = impedensi[i] - impedensi[i-1] / impedensi[i] + impedensi[i-1]
    r.append(R)
    print("RC ke-",i,":",R)
print(r)

# Z[i+1] = Z[i]((1 + r[i])/(1 - r[i])) inversi metode rekursif
z = []
for i in range(len(impedensi)) and range(len(r)):
    inversi = impedensi[i] * (1 + r[i] / 1 - r[i])
    z.append(inversi)
    print("Inversi ke-",i,":",inversi)
print(z)

def litologi():
    
    for i in range(len(kec_gel_p)):
        if kec_gel_p[i] > 2000 and densitas[i] == 2:
            print("Litologi batuan Sandstone")
        elif kec_gel_p[i] <= 2000 and densitas[i] == 1.95:
            print("Litologi batuan Sandstone")
        else:
            print("Batu Ginjal")
        
litologi()

    
def batas():
    for i in range(len(impedensi)-1):
        if impedensi[i] == impedensi[i+1]:
            print("Bukan Batas Litologi")
        else:
            print("Batas Litologi")

batas()

#berupa data user, impedansi akustik, koefisien refleksi, hasil inversi seismik, j
# enis litologi batuan, dan informasi batas litologi batuan

# format teks
teks = "Nama: {}\nTanggal: {}\nTempat: {}\nNama Lintasan: {}\nImpedansi: {}\nKoefisien Refleksi: {}\nInversi: {}\nLitologi: {}\nBatas Litologi: {}".format(y.nama,y.tanggal,y.tempat,y.get_nama_lintasan(),impedensi,r,z,litologi,batas)

# buka file untuk ditulis
file = open("Seismik.txt", "w")

# tulis teks ke file
file.write(teks)

# tutup file
file.close()







