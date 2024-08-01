### PythonProject in input-for-if_else-range-print

### 1-	İki sayının (a,b) durumuna göre şu işlemi yapacaktır. a>b ise 2*a+b-3, b>a ise 2*b+a-3, a=b ise a*b yapacaktır. Bu işlemi yapan programı yazınız? italik metin:

a=int(input("bir a sayısı giriniz:"))
b=int(input("bir b sayısı  giriniz:"))
if(a>b):
 islem=2*a+b-3
elif(b>a):
 islem=2*b+a-3
else:
 islem=a*b

print(islem)


##2- Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren programı yazınız?

maas=int(input("maaş:"))
zam_orani=int(input("zam oranı %"))
zamli_maas=(((maas*zam_orani)/100)+maas)
print(zamli_maas)

## 3- 100 arası 3 e ve 5 e tam bölünen sayıları yazınız?

for i in range(1,101):
 if(i%15==0):
  print(i)

#sigma toplam işlemini göstere bir simgedir. Denkleme göre 2 den n kadar sayılarla işlem yapılacaktır) n dışarıdan girilecektir. n’nin değeri kesinlikle i’nin başlangıç değerinden büyük olması gerekmektedir. Bu işlemi yapan programı yazınız?

n=int(input("bir n değeri giriniz:"))
if (n>2):
   for i in range(2,n):
     islem=(i-1)/i
   print(islem)
else:
  print("!! n değeri 2 den küçük veya eşittir tekrar giriniz.")


for i in range(1,36):
 islem=35*i
 print("35",i,islem)

 # -------------------
 say=int(input("s gir"))   #input girişi anlatan yorum satırı
ctop=0
ttop=0

for i in range(1,say+1):
  if(i%2==0):
     ctop=ctop+i

  else:
    ttop=ttop+i

  print("tek say toplamı= {0} çift say toplamı= {1}".format(ttop,ctop))
#-------------------

x= int(input("sayı giriniz:"))
for i in range(1,x+1):
  print(i)

#-------------------
for say in range(2,101,2):
  print(say)

#-------------------
a=int(input("a:"))
b=int(input("b:"))

top=0
for i in range(a,b):
  top=top+i

print("top",top)
