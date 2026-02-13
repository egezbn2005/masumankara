print("Sayı Tahmin Oyununa Hoş Geldin!")
import random

def oyun():
    hedef_sayi = random.randint(1, 100)
    deneme_sayisi = 0
    
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

    while True:
        tahmin = int(input("Tahminin nedir?: "))
        deneme_sayisi += 1

        if tahmin < hedef_sayi:
            print("Daha büyük bir sayı söyle!")
        elif tahmin > hedef_sayi:
            print("Daha küçük bir sayı söyle!")
        else:
            print(f"Tebrikler! {deneme_sayisi}. denemede buldun.")
            break

oyun()