hasil_akhir = [
    {"nama":"Reza", "nilai": 70},
    {"nama":"Ciut", "nilai": 63},
    {"nama":"Dian", "nilai": 80},
    {"nama":"Badu", "nilai": 40}
]
print("Yang Lulus adalah:")

def lulus_saja(hasil_akhir):
    for i in hasil_akhir:
        if i["nilai"] > 65 :
            lulus = i["nama"]
            print(lulus, end=" ")
lulus_saja(hasil_akhir)