nilai_kec_gel = int(input("Masukan nilai kecepatan gelombang P : "))

if nilai_kec_gel in range(328,1640):
    print("Kecepatan sebesar" ,nilai_kec_gel, "maka batuan Clay ")
elif nilai_kec_gel in range(656,6561):
    print("Kecepatan sebesar" ,nilai_kec_gel, "maka batuan Sand ")
elif nilai_kec_gel in range (3281,8202):
    print("Kecepatan sebesar" ,nilai_kec_gel, "maka batuan Lempung ")
else:
    print("Kecepatan sebesar" ,nilai_kec_gel, "tidak ada dalam if elif else nya ")

