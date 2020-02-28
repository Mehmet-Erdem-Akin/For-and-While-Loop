# WHİLE DÖNGÜLERİ UYGULAMALAR

# Sayılar listesinin elemanlarını tek tek ekrana yazdırın?
"""
sayilar = [1,4,8,13,17,19,24,25]

sayi = 0
while sayi < len(sayilar):
    print(sayilar[sayi])
    sayi += 1
"""
# Kullanıcıdan aldığımız iki değer arasındaki çift sayıları ekrana yazdırın?
"""
ilk = int(input("başlangıç değeri : "))
son = int(input("bitiş değeri : "))

while ilk <= son:
    ilk += 1
    if ilk % 2 == 0:
        print(ilk)
"""

# 1 ile 100 arasındaki sayıları azalacak şekilde ekrana yazdırın?
"""
sayi = 100
while sayi > 1:
    sayi -= 1
    print(sayi)
"""


# Kullanıcıdan 5 adet sayı alarak bunları sıralı olarak bir listeye atın? # HATALI !!!!!!!!11
"""
sayilar = []
sayi = 0

while sayi<5:
    sayi = int(input('sayı giriniz : '))
    sayilar.append(sayi)
    sayi += 1
#sayilar.sort()
print(sayilar)
 """  










