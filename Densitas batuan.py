nilai_densitas_batu = float(input("Nilai Densitas Batuan Sedimen : "))

if nilai_densitas_batu in (1.96,2):
   print("Batuan yang memiliki nilai densitas sebesar",nilai_densitas_batu, "adalah Batu Alluvium")
elif nilai_densitas_batu in (1.63,2.6):
    print("Batuan yang memiliki nilai densitas sebesar",nilai_densitas_batu, "adalah Batu Clay")
elif nilai_densitas_batu in (1.93,2.9):
    print("Batuan yang memiliki nilai densitas sebesar",nilai_densitas_batu, "adalah Batu Limestone")
elif nilai_densitas_batu in (2.28,2.9):
    print("Batuan yang memiliki nilai densitas sebesar",nilai_densitas_batu, "adalah Batu Dolomite")
else:
   print("Nilai densitas sebesar" ,nilai_densitas_batu, "tidak ada dalam if elif else nya ")



