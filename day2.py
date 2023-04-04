faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

# print(vade + 12)
print(int(vade) + 12)
# print(int(krediAdi)) - int olamayacak tipler yazdigimizda hata aliriz

faiz = str(faiz)
print(type(faiz))

# int yukarida olursa
vade = int(input("Lütfen istediğiniz vade sayısını girin: "))
print(type(vade))
print(vade + 12)
vade = vade + 12

# int asagida olursa
# vade = 36 # input("Lütfen istediğiniz vade sayısını girin: ")
# print(type(vade))
# print(int(vade) + 12)

# string interpolation
# Sectiginiz vade sonucu ortaya cikan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = 15))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}")

isim = "Halit"
metin = "Merhaba {name}".format(name = "Samet")
print(metin)

isim = "Halit" # input("Isminizi giriniz: ")
metin = "Merhaba {name}".format(name = isim)
print(metin)

yash = 32
sonuc = "Yashiniz {benimYashim}".format(benimYashim = yash + 2)
print(sonuc)

ad = "Feride"
metin1 = "Merhaba {adim}".format(adim = ad)
print(metin1)

# f-string
metin = f"Hoşgeldiniz {isim}"
print(metin)

metin = f"Hoşgeldiniz {1+1}"
print(metin)


# listeler
# donguler

# Python'da listedeki tiplerin hepsi ayni olmak zorunda degil
dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

print(len(krediler))

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop() # veya pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

krediler.copy() # listenin aynisini veriyor
print(krediler)

print("      ")

krediler.clear() # listeyi siliyor
print(krediler)

# for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)

print("**********")

x = 15
for i in range(5, x):
    print(i)

print("**********")

for i in range(5, 10):
    print(i)

print("**********")

for i in range(10, 51, 10):
    print(i)

print("**********")

# for'da yalniz int yazmamiz lazim, float degil
# for i in range(0.1, 0.5):
#     print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("**********")

for i in range(len(krediler)): # range(3)
    print(krediler[i])         # krediler[0] krediler[1] krediler[2]

print("**********")

# sonsuz dongu
i = 0
while i < 10:
    print("x")
    i += 1
print("y") # buraya hic bir zaman yetismiyor, cunki yukarisi sonsuz dengi ile devam ediyor

print("**********")

while True:
    print("XYZ")
    break

print("**********")

i = 0
while i < len(krediler):
    print(i)
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break


# fonksiyonlar

fiyat = 100
indirim = 20

# definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat - indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)
sayHello("Halit")

print("**********")

# geriye bir sey donmesi gerektigi zaman return kullaniyoruz
def calculateAndReturn(price, discount):
    return price - discount
# return kismina liste de yazabiliriz: return ["1", "2"]

yeniFiyat = calculateAndReturn(200, 50)
print(yeniFiyat + 10)

print("***** Print ile Return farki *****")

def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("fonk1 sonucu:")
fonk1 = calculatePrice(100, 50)

print("fonk2 sonucu:")
fonk2 = calculatePriceAndReturn(300, 100)

print("print fonk1:")
print(fonk1)

print("print fonk2")
print(fonk2)

# veya
# print(f"200. satir: {fonk1}")
# print(f"160. satir {fonk2 + 100}")
# 1. fonksiyonda sadece anlik olarak print kullanip onun sonucunu bize verir, ama onu baska yerlerde kullanamiyoruz. Ama 2. fonksiyon o anda print etmese de bize bir deger return ettigi icin onu baska yerde calistirdigimiz zaman bize o degeri verir. Bunun icin {fonk2 + 100} olarak da kullanabiliriz, cunki fonk2 bir deger veriyor bize, onun uzerine 100 ekliyor

