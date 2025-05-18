
import random 
sehirler = ["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik",
"Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ",
"Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin",
"İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya",
"Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt",
"Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray",
"Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye",
"Düzce"]

print("Şehir ismi tahmin etme oyununa hoşgeldin!\nBu oyunda algoritma sana sistemden rastgele bir şehir ismini verecek ve\nharf tahminlerinle "\
"şehir ismini doğru tahmin etmeye çalışacaksın! Her şehir için toplam hata hakkın 4, iyi eğlenceler!")

basla = int(input("Başlamak için 0'a bas! "))
yanlis=0

if basla == 0:
   kelime = random.choice(sehirler).lower()
   harfler = list(kelime)
   sifreli = ["?"]*len(harfler)
   uzunluk = len(kelime)
   print(*sifreli)
   print("Tahmin edeceğin kelime",uzunluk,"harften oluşuyor.")
 
   while yanlis<5 and "?" in sifreli:
      tahmin = input("Harf tahminini gir veya tüm kelimeyi tahmin etmek için 1'i tuşla. ").lower()

      if tahmin== "1":
         sonuc = str(input("Tahmininizi girin!" )).lower()
         if sonuc==kelime:
            print("Tebrikler, doğru kelime:", kelime)
            break
         else:
            yanlis+=1
            print("Yanlış tahmin, hata sayın:", yanlis)

      elif tahmin in harfler:
         for i in range(len(harfler)):
            if harfler[i]==tahmin:
              sifreli[i] = tahmin
         print(*sifreli)  

      else:
         yanlis+=1
         print("Girdiğin harf kelimede geçmiyor. Hata sayın:",yanlis)
         print(*sifreli)
    
   if "?" not in sifreli:
      print("Tebrikler, doğru tahmini yaptın!")

   elif yanlis>=5:
      print("Hata yapma haklarını doldurdun, doğru kelime:",kelime)




   
         

      
     
