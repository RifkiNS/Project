nilai_susep_batu = int(input("Nilai Suseptibilitas Magentik Batuan Beku :"))


if nilai_susep_batu in range(0,4000):
            print("Batuan yang memiliki nilai suseptibilitas sebesar",nilai_susep_batu, "adalah Batu Granit")
elif nilai_susep_batu in range(20,14500):
            print("Batuan yang memiliki nilai suseptibilitas sebesar" ,nilai_susep_batu, "adalah Batu Basal") 
elif nilai_susep_batu in range(50,10000):
            print("Batuan yang memiliki nilai suseptibilitas sebesar" , nilai_susep_batu, "adalah Batu Diorit")
else:
     print("Nilai suseptibilitas sebesar" ,nilai_susep_batu, "tidak ada dalam if elif else nya ")
