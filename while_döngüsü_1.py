"""
x = 0 # 1 yazarsak 1 den baþlar 
while x <= 100:
    print(x)
    x = x + 1 # veya x += 1 yazabiliriz 
"""

# while döngüsü ile for gibi bir deðiþken tanýmlayarak koyduðumuz þarta ulaþana kadar yazdýrma iþlemi yapabiliriz.

"""
x = 1 
while x <= 100:
    if x % 2 == 0: # x in 2 ye bölümünden kalan 0 a eþit ise x i yazdýr. Tek sayýlarý istersek 1 yazardýk.
        print(x)
x += 1
"""

"""
Burada x e 1 deðerini verdik, bu while ile x 100 e eþit ve küçük olduðuna kadar döndürülecek demektir.
if ile eðer x in 2 ye bölümünden kalan 0 a eþit ise x i yazdýr dedik 
son satýr ile x i 1 arttýrarak döngüyü baþa aldýk
"""

"""
x = 1 
while x <= 100:
    if x % 2 == 0: # eðer x in 2 ye bölümünden kalan 0 a eþit ise çift sayý : x i yazdýr. 
        print("çift sayý : "+str(x))
    else:
        print("tek sayý : "+str(x)) # Diðer durumlarda ise tek sayý : x þeklinde yazdýr
    x += 1
print("iþlem bitmiþtir...")
"""



