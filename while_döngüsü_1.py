"""
x = 0 # 1 yazarsak 1 den ba�lar 
while x <= 100:
    print(x)
    x = x + 1 # veya x += 1 yazabiliriz 
"""

# while d�ng�s� ile for gibi bir de�i�ken tan�mlayarak koydu�umuz �arta ula�ana kadar yazd�rma i�lemi yapabiliriz.

"""
x = 1 
while x <= 100:
    if x % 2 == 0: # x in 2 ye b�l�m�nden kalan 0 a e�it ise x i yazd�r. Tek say�lar� istersek 1 yazard�k.
        print(x)
x += 1
"""

"""
Burada x e 1 de�erini verdik, bu while ile x 100 e e�it ve k���k oldu�una kadar d�nd�r�lecek demektir.
if ile e�er x in 2 ye b�l�m�nden kalan 0 a e�it ise x i yazd�r dedik 
son sat�r ile x i 1 artt�rarak d�ng�y� ba�a ald�k
"""

"""
x = 1 
while x <= 100:
    if x % 2 == 0: # e�er x in 2 ye b�l�m�nden kalan 0 a e�it ise �ift say� : x i yazd�r. 
        print("�ift say� : "+str(x))
    else:
        print("tek say� : "+str(x)) # Di�er durumlarda ise tek say� : x �eklinde yazd�r
    x += 1
print("i�lem bitmi�tir...")
"""



