#RUN LENGTH ENCODING(RLE) - PYTHON

#bu fonksiyon gelen metni sıkıştırır
def rle_sikistir(metin):
    #eğer kullanıcı boş bir metin girerse direkt boş döndürür.
    if metin == "":
        return ""
    
    sonuc = ""
    #sıkıştırılmış sonucu tutacak olan ifade
    sayac = 1
    #aynı karakterin ardışık kaç kez tekrar ettiğini tutan ifade
    
    #1.karakterden başlayarak tüm metni gezdirir
    for i in range(1,len(metin)):
        #eğer şuanki karakter bir önceki karakter ile aynı ise;
        if metin[i] == metin[i-1]:
            sayac+=1
            #sayacı arttır
        else:
            #şuanki karakter önceki karakter ile aynı olmadığında yani karakter değiştiği an;önceki karakter ve tekrarı sonuca eklenir.
            sonuc += str(sayac) + metin[i-1]
            sayac=1  #sayaç sıfırlanır.(yeni karakter için 1 sayılır.)
    
    #döngü bitince son karakteri de eklememiz gerekir.
    sonuc += str(sayac) + metin[-1] 
    return sonuc

#bu fonksiyon sıkıştırılmış metni eski haline döndürür.
def rle_ac(metin): 
    sonuc=""    #açılmış metin
    sayi=""     #karakterin önündeki rakamı tutar
    
    for karakter in metin:
        if karakter.isdigit():
            sayi += karakter
            #eğer karakter bir rakam ise sayı birikir
        else:
            sonuc += karakter * int(sayi)
            sayi = ""    #sayı sıfırlanır
            #eğer harfe geldiysek harfi sayısı kadar ekrana yazdırır.
    return sonuc
 
#sıkıştırma oranını hesaplayan fonksiyon
def oran_hesapla(orijinal,sıkıştırılmış):
    return (len(orijinal)/len(sıkıştırılmış))






#kullanıcı girişi
metin = input("sıkıştırmak istediğiniz metni girin: ")

#fonksiyonları çağırarak işlemleri yaptırır.
s = rle_sikistir(metin)     #sıkıştırılmış metin
a = rle_ac(s)               #geri açılmış hali




#sonuç yazdırma
print("\n ------SONUCLAR-----")
print("orijinal: ",metin)
print("sıkıştırılmış: ",s)
print("açılmış hali: ",a)
print("sıkıştırma oranı: ",oran_hesapla(metin,s))
