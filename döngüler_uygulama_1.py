sayilar = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)

# Hangi sayılar 4'ün katıdır?
"""
for sayi in sayilar:
    if sayi%4 == 0:
        print(sayi)
"""
# Sayılar listesindeki tüm sayıların toplamı kaçtır?
"""
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi #toplam += sayi 
print(toplam)
"""

# Sayılar listesindeki tek sayıların karesini Nedir ?
"""
for sayi in sayilar:
    if sayi%2 == 1:
        print(sayi**2)


dersler = ["Matematik","Türkçe","Biyoloji","Edebiyat","Fen"]
"""

# Yukarıdaki listeye göre karakter uzunlukları 6'yı geçmeyen dersler hangileridir ? 
"""
for ders in dersler:
    if len(ders) <= 6:
        print(ders)

araclar = [
    {"fiat":"linea", "fiyat":"30000"},
    {"renault":"broadway", "fiyat":"10000"},
    {"ford":"fiesta", "fiyat":"40000"},
    {"hyundai":"accent", "fiyat":"35000"},
]
"""

# Örneğin elimize satılan araçlara dair bir veri geldi ve bizden toplam satış fiyatı istenmekte. 
"""
toplam = 0
for arac in araclar:
    toplam = toplam + int(arac["fiyat"])
print("Toplam Satış Fiyatı : "+str(toplam))

personeller = [
    {"İsim":"Mehmet", "maaş":"3250"},
    {"İsim":"Gülcan", "maaş":"4500"},
    {"İsim":"Güler", "maaş":"2600"},
    {"İsim":"Erdem", "maaş":"2900"},
]
"""

# Örneğin elimize personeller ve maaşlarına dair bir veri geldi ve bizden maaşı 3000 tl'nin üstünde olan personeller isteniyor.
"""
for personel in personeller:
    if (int(personel["maaş"]) >= 3000):
        print(personel["İsim"])
"""
