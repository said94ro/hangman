# 4 hakki olsun 


import random

kelimeler = ["tufek"]
kalan_Hak = 4
ilk_kelime=random.choice(kelimeler)
tahmin="_ "*len(ilk_kelime)
bulunan_harf=""
kelime_indexed =[]
kulanilan_harf=[]

for x, index in enumerate(ilk_kelime):
    kelime_indexed.append((x,index))
print(kelime_indexed)

while kalan_Hak != 0:
    
    print(bulunan_harf)
    print(tahmin)    
    print(f"Kalan hak:{kalan_Hak}")
    harf=input("harf lutfen: ")
    if harf not in kulanilan_harf:
        kulanilan_harf.append(harf)
        if harf not in ilk_kelime:
            kalan_Hak -= 1
        else:
            for harfx in kelime_indexed:
                if harfx[1] == harf:
                    print(f"DOGRU TAHMIN: {harf} ")

                    bulunan_harf = bulunan_harf[:harfx[0]] + harfx[1] + bulunan_harf[harfx[0]:]
    else:
        print(
            "Bu harf kulanildi"
        )
        












