print('-'*15, 'Pengeluaran Harian', '-'*15)

import datetime as dt


def Date():
    #Tanggal = int(input('Tanggal\t:'))
    #Bulan = int(input('Bulan \t:'))
    #Tahun = int(input('Tahun \t:'))
    date = dt.date.today()
    print(date)
    
def Barang_Harga():
    item = int(input('Masukkan Banyaknya Barang:'))
    harga = []
    for i in range(item):
        Barang = input('Masukkan Barang Belanja\t:')
        Harga = float(input('Masukkan Harga Barang:'))
        print(Barang, 'Rp','{0:.3f}'.format(Harga))
        harga.append(Harga)
    Total = sum(harga)
    print('Total Belanja\t: ','{0:.3f}'.format(Total))
    

Date()
Barang_Harga()


    
        

        

