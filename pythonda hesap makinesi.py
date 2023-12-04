class islem():
    def __init__(self,ilksayi,ikincisayi=1):
        self.sayi1=ilksayi
        self.sayi2=ikincisayi

    def topla(self):
       return self.sayi1+self.sayi2
    def cıkar(self):
       return self.sayi1-self.sayi2
    def carp(self):
        return self.sayi1*self.sayi2
    def bol(self):
        if(self.sayi2!=0):
            return self.sayi1/self.sayi2
        else:
            return "hata"
    def usal(self):
        return self.sayi1**self.sayi2
    def faktoriyel(self):
        f=1
        while(self.sayi1!=0):
            f *= self.sayi1
            self.sayi1 -= 1
        return f
    def kalanbul(self):
        return self.sayi1 % self.sayi2
    def karekok(self):
        return self.sayi1**(1/2)


while(1):
    print("1. toplama\n2. cikarma\n3. carpma\n4. bolme\n5. usalma\n6. faktoriyel alma\n7. kalan bulma\n8. karekok bulma\nlutfen bir secim yapın")
    secim = int(input())
    if (secim > 8 or secim < 1):
        print("hatalı secim")
    elif(secim==6 or secim==8):
        print("sayiyi girin")
        asayisi = int(input())
        bsayisi = None
    else:
        print("ilk sayiyi girin")
        asayisi = int(input())
        print("ikinci sayiyi girin")
        bsayisi = int(input())





    i1 = islem(asayisi, bsayisi)

    if (secim == 1):
        print("sonuc :", i1.topla())
    elif (secim == 2):
        print("sonuc :", i1.cıkar())
    elif (secim == 3):
        print("sonuc :", i1.carp())
    elif (secim == 4):
        print("sonuc :", i1.bol())
    elif (secim == 5):
        print("sonuc :", i1.usal())
    elif (secim == 6):
        print("sonuc :", i1.faktoriyel())
    elif (secim == 7):
        print("sonuc :", i1.kalanbul())
    elif (secim == 8):
        print("sonuc :", i1.karekok())



