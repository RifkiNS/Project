from collections import deque

#Antrian pemesan
pemesanan = input('Nama :')
def antrian():
    nomor_antri = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,16,17,18,19,20])

    out = nomor_antri.popleft()
    print('nomor antrian anda:',out)



antrian()    

print('-'*10, 'Silahkan Pilih Menu','-'*10)

#Menu Makanan Dan Minuman
def Menu_Makanan():
    print("="*5, ' Menu Makanan', '='*5,
          '\n1. Nasi Ayam Geprek\t  :12.0000',
          '\n2. Nasi Soto Ayam\t  :10.000',
          '\n3. Nasi Ayam Penyet\t  :13.000', 
          '\n4. Nasi Ayam Geprek Besar :15.000')

def Menu_Minuman():
    print("="*5, ' Menu Minuman', '='*5,
          '\n1. Es Teh Manis\t  :4.0000',
          '\n2. Es Jeruk Peras:5.000',
          '\n3. Es Kopi\t  :4.000', 
          '\n4. Kopi/Teh Panas :3.000')
    

 
Menu_Makanan()
Menu_Minuman()

#Order makanan dan minuman
jumlah_order = int(input('Jumlah Orderan:'))
Total = []
    
for i in range (jumlah_order):
    order_makanan = int(input('Pilih Menu Yang Ingin dipesan:'))
    porsi = int(input('Untuk Berapa Porsi:'))
    if order_makanan==1:
        total = porsi*12000
        pesanan = ('Nasi Ayam Geprek')
        print(pesanan,'= Rp.', total) 
        Total.append(total)
    elif order_makanan==2:
        total = porsi*10000
        pesanan = ('Nasi Soto Ayam ')
        print(pesanan,'= Rp.', total)
        Total.append(total)
    elif order_makanan==3:
        total = porsi*13000
        pesanan = ('Nasi Ayam Penyet')
        print(pesanan,'= Rp.',total)
        Total.append(total)
    elif order_makanan==4:
        total = porsi*15000
        pesanan = ('Nasi Ayam Geprek Besar')
        print(pesanan,'= Rp.', total)
        Total.append(total)
#print(Total)

#jumlah_order = int(input('Jumlah Orderan:'))

Total_minum = []   

for i in range (jumlah_order):
    order_minuman = int(input('Pilih Minuman:'))
    porsi = int(input('Berapa Gelas:'))
    if order_minuman==1:
        totalminum = porsi*4000
        pesanan_minuman = ('Es Teh Manis')
        print(pesanan_minuman,'= Rp.', totalminum)
        Total_minum.append(totalminum) 
    elif order_minuman==2:
        totalminum = porsi*5000
        pesanan_minuman = ('Es Jeruk Peras ')
        print(pesanan_minuman,'= Rp.', totalminum)
        Total_minum.append(totalminum) 
    elif order_minuman==3:
        totalminum = porsi*4000
        pesanan_minuman = ('Es Kopi')
        print(pesanan_minuman,'= Rp.', totalminum)
        Total_minum.append(totalminum) 
    elif order_minuman==4:
        totalminum = porsi*3000
        pesanan_minuman = ('Kopi/Teh Panas')
        print(pesanan_minuman,'= Rp.', totalminum)
        Total_minum.append(totalminum) 
#print(Total_minum)    






#Bill Makanan dan Minuman
bayar = sum(Total) + sum(Total_minum)

print("\nYang Harus Dibayarkan:",bayar)
uang_masuk = int(input('Sebesar = Rp '))
uang_kembalian = int(uang_masuk-bayar)
print('Kembalian : Rp',uang_kembalian)

# struck pembelian
print('-'*10,'Struck Pembelian', '-'*10)
print('\nNama Pembeli\t\t:', pemesanan)
print('\nRincian Belanja\t\t:', porsi, pesanan,total,
      '\n','\t\t\t',porsi, pesanan_minuman,totalminum)
print('\nTotal \t\t\t:', bayar)
print('\nUang Yang Dibayarkan\t:',uang_masuk)
print('\nUang Kembalian\t\t:', uang_kembalian)
print('\nTerimakasih Sudah Berkunjung')