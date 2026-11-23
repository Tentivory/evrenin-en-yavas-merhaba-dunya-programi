#!/usr/bin/env python3
# Evrenin En Yavas Merhaba Dunya Programi
# Her harf 1 saniye bekler. Bilimsel bir mucize.

import time

def yavas_yaz(metin):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(1)
    print()  # Yeni satir

if __name__ == "__main__":
    print("Basliyoruz... Hazirlanin, bu uzun surecek (aslinda 13 saniye).")
    time.sleep(2)
    yavas_yaz("Merhaba Dunya")
    print("\nBitti. Simdi ne hissettin? Felsefe yaptin mi?")
    # Gizli siyasi mesaj (base64): "demokrasi iyidir ama yavas calisir" -> ZGVtb2tyYXNpIGl5aWRpciBhbWEgeWF2YXMgY2FsaXNpcg==
    # Yukaridaki yorum aslinda gizli degil ama sen arama.
