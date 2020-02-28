"""
number =  [1,2,3,4,5]

for num in number:
    print(num)
"""
#number içindekileri tek tek num'a atar ve her atandığında döndürür. Dönme işlemi eleman sayısı bitene kadar devam eder.

"""
number =  [1,2,3,4,5]

for num in number:
    print(number)
"""
# Eğer num yerine number'ı yazdırırsak [1,2,3,4,5] değerini yazdırır ve eleman sayısı kadar döndürür.

"""
number =  [1,2,3,4,5]

for num in number:
    print(num)
    print(number)
"""

"""
Buranın çıktısı 1 kez numberı yazdırır [1,2,3,4,5] sonra num içinden 1 yazdırır. 
Dahasonra tekrar number sonra num içindeki ikinci değeri
"""

"""
isimler = ["Mehmet","Erdem","Akın"]
    
for isim in isimler:
    print("Benim Adım : " + isim)
"""

# Yazdırma işlemi yaparken bu şekilde string bir ifade ile birleştirebilirsiniz.
    
"""
isim = "Mehmet Erdem Akın"

for i in isim:
    print(i)
"""

# Eğer liste yerine string bir değeri döngüye alırsanız python string ifadenin her bir karakterini döndürecektir.
# NOT: Boşluklar da buna dahildir.

"""
sözlük = {"bir":1, "iki":2,"üc":3}

for s in sözlük:
    print(s)
"""
# Sözlük biçimini döngüde kullanırsak anlamlarını yazdıracaktır.

"""
sözlük = {"bir":1, "iki":2,"üc":3}

for s, anlam in sözlük.items():
    print(s, anlam)

# Fakat hem kelimeyi hem de anlamını yazdırmak istiyorsak bu şekilde yazarız
"""












