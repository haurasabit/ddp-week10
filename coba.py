#ARRAY
# berisi ssekumpulan data dengan urutan tertentu
#bisa ada duplikasi
#diakses dgn indeks
#list di python merupakan implementasi dari array
nilai = [65, 60, 75, 0, 98]
print (nilai [0] == 65)
print (nilai [len(nilai) -1])


# STACK
# last in first out --> punya 2 operasi:
# PUSH utk menyimpan data ke atas tumpukan
# POP utk mengambil data yg paling atas
#list di python juga mendukung operasi stack:
# APPEND utk push & POP
bilangan = [1,2,4]
a = bilangan.pop()
bilangan.append(6)
print(bilangan)
print(a)


# QUEUE
#it means antrian
# struktur data FIFO (pertama masukin berarti pertama diambil)
# ada 2 perintah : ENQUEUE (masukin ke antrian), DEQUEUE (mengambil dr antrian)
# python list jg bisa dipakai utk queue
angka = [1,3,6]
angka.append(0)
a = angka.pop(0)
print(a)


# SET --> himpunan
# tdk ada duplikasi, tdk jamin urutan
# dituliskan dgn {}
f = {11, 12, 13}
print(f)
# menambahkan dgn add
# menghapus dgn remove
# mengambil elemen terakhir dgn pop, tp tdk ada jaminan elemen mana yg akan diambil
f.add(3)
f.add(15)
f.remove(12)
print (f.pop())
print(f)

#SET
#menggabungkan dgn union
set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union (set2)
print(set3)
#memasukkan dgn update
set4 = {1,2,3}
set5 = {2,4,6}
set4.update (set5)
print(set4)


# DICTIONARY
#utk menyimpan data yg diakses bukan dgn indeks
#data yg disimpan dr key dan value
# dituliskan dgn diapit kurung krawal {} ,
# dan dipisah dgn titik dua
data_diri = {
    "nama":"haura",
    "matkul":"python" 
}
data_diri["semester"] = 1 
print(data_diri["nama"])

#mengakses dgn key, ex:
p = data_diri["nama"] #bisa jg data_diri.get("nama")
#mengubah value
data_diri["nama"] = "scara"
#menambah entri
data_diri["alamat"] = "Jakarta"
#menghapus key
data_diri.pop("alamat")

#mengecek keberadaan key, pakai operator in
if("nama" in data_diri):
    print("nama ada di data_diri")
    

# LIST
#berisi sekumpulan data dgn urutan tertentu
#bisa ada duplikasi
#array bisa merupakan implementasi dr list
#implementasi dari : LinkedList
#  tdk bisa diakses dgn indeks
#  memiliki akses ke entri pertama (biasanya "head")
#  tiap entri memiliki nilai (value) & link entri berikutnya (next)
