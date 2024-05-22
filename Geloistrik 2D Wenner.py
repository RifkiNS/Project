spasi_elektroda = float(input("Spasi elektroda: "))
n = int(input("Nilai n: "))
i = float(input("Nilai arus: "))
v = float(input("Nilai tegangan: "))
sp = float(input("Nilai sp: "))

# membuat fator geometri (nilai K)
faktor_geometri = 2*3.14*n*spasi_elektroda
print("Faktor geometri: ",faktor_geometri)

# mencari nilai Delta V
del_v = v - sp
print("Perubahan tegangan: ", del_v)

# resis semu
res_semu = faktor_geometri*del_v/i
print("Resistivitas semu: ", res_semu)

# perintah mengulang pengambilan data
if res_semu > 0:
    print("lanjut ke datum selanjutnya")
else:
    print("ulangi pengambilan data")