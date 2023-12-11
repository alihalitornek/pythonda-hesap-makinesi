class islem():
    def __init__(self,ilksayi,ikincisayi):
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
        if (self.sayi2 in range(0, 100) and self.sayi1 in range(0, 1000)):
            return self.sayi1**self.sayi2
        elif (self.sayi2 in range(0, 20) and self.sayi1 in range(0, 100000000)):
            return self.sayi1 ** self.sayi2
        else:
            return "sonsuz"
    def faktoriyel(self):
        if(self.sayi1<0):
            return "hata"
        elif (self.sayi1 not in range(0, 1000)):
            return "sonsuz"
        else:
            f=1
            while(self.sayi1!=0):
                f *= self.sayi1
                self.sayi1 -= 1
            return f
    def kalanbul(self):
        if (self.sayi2 != 0):
            return self.sayi1 % self.sayi2
        else:
            return "hata"
    def karekok(self):
        return self.sayi1**(1/2)

asayisi = None
bsayisi = None

while(1):
    kontrol = "hata"
    while(kontrol == "hata"):
        print("1. toplama\n2. cikarma\n3. carpma\n4. bolme\n5. usalma\n6. faktoriyel alma\n7. kalan bulma\n8. karekok bulma\nlutfen bir secim yapın")
        secim = input()
        if (secim > "8" or secim < "1"):
            print("hatali secim")
        elif(secim=="6" or secim=="8"):
            print("sayiyi girin")
            try:
                asayisi = int(input())
            except:
                print("hatali giris")
                kontrol="hata"
            else:
                kontrol="dogru"

        elif(not(secim=="6" or secim=="8")):
            try:
                print("ilk sayiyi girin")
                asayisi = float(input())
                print("ikinci sayiyi girin")
                bsayisi = float(input())
            except:
                print("hatali giris")
                kontrol = "hata"
            else:
                kontrol="dogru"
        else:
            print("hatali giris")





    i1 = islem(asayisi, bsayisi)

    if (secim == "1"):
        print("sonuc :", i1.topla())
    elif (secim == "2"):
        print("sonuc :", i1.cıkar())
    elif (secim == "3"):
        print("sonuc :", i1.carp())
    elif (secim == "4"):
        print("sonuc :", i1.bol())
    elif (secim == "5"):
        print("sonuc :", i1.usal())
    elif (secim == "6"):
        print("sonuc :", i1.faktoriyel())
    elif (secim == "7"):
        print("sonuc :", i1.kalanbul())
    elif (secim == "8"):
        print("sonuc :", i1.karekok())



