def lowest_multiple(a,b):
    if(a>b):
        i=a
    if(b>a):
        i=b
    else:
        i=a
    multiplu=0
    found_number = False
    while found_number == False:
        if(i%a==0 and i%b==0):
            found_number = True
            multiplu = i
        else:
            i+=1
    return print("Cel mai mic multiplu comun a",a,"si",b,"este:", i)

def sum(a,b):
    return print("Suma:",a,"+",b,"=",a+b)

def prod(a,b):
    return print("Produsul:",a,"x",b,"=",a*b)

def media(a,b):
    return print("Media aritmetica a numerelor:",a,"si",b,"este:",(a+b)/2)

def biggest_div(a,b):
    cel_mai_mare_divizor=0
    if(a>b):
        i=b
    if(b>a):
        i=a
    else:
        i=a
    while(i>1):
        if(a%i==0 and b%i==0):
            cel_mai_mare_divizor = i
            break
        i-=1
    if(i<=1):
        cel_mai_mare_divizor = "aceste numere nu au divizoare comune in afara de 1"
        return print(cel_mai_mare_divizor)
    return print("cel mai mare divizor comun a",a,"si",b,"este:",i)
    
def max_min(a,b):
   return print("Cel mai mare numar e:",max(a,b),"\nCel mai mic numar e:",min(a,b))

def common_div(a,b):
    common_divisors=[]
    if(a>b):
        i=b
    if(b>a):
        i=a
    else:
        i=a
    while(i>0):
        if(a%i==0 and b%i==0):
            common_divisors.append(i)
        i-=1
    print("Toti divizorii comuni: ",end="")
    for i in range(0,len(common_divisors)):
        if(i==len(common_divisors)-1):
            print(common_divisors[i])
        else:
            print(common_divisors[i],end=",")
    return 0

def common_multiple_5(a,b):
    multipli=[]
    if(a>b):
        i=a
    if(b>a):
        i=b
    else:
        i=a
    multiplu=0
    while len(multipli)<5:
        if(i%a==0 and i%b==0):
            multipli.append(i)
            i+=1
        else:
            i+=1
    return print("5 multipli comuni:",multipli)

def common_numbers(a,b):
    common=[]
    a=str(a)
    b=str(b)
    if(len(a)>len(b)):
        longest=a
        shortest=b
    else:
        longest=b
        shortest=a
    for num in shortest:
        for num1 in longest:
            if (num == num1):
                common.append(num)
    common=list(dict.fromkeys(common))
    return print("Toate cifrele comune:",common)

def uncommon_numbers(a,b):
    iscommon=False
    notcommon=[]
    a=str(a)
    b=str(b)
    for num in a:
        for num1 in b:
            if (num == num1):
                iscommon=True
        if(iscommon==False):
            notcommon.append(num)
        iscommon=False
    notcommon=list(dict.fromkeys(notcommon))
    return print("toate cifrele care sunt in "+a+" si nu sunt in "+b+" :",notcommon)

def prietene(a,b):
    a_d=0
    b_d=0
    for i in range(1,a+1):
        if(a%i==0):
            a_d+=1
    for z in range(1,b+1):
        if(b%z==0):
            b_d+=1
    if b_d==a_d:
        return print("Aceste numere sunt prietene!")
    else:
        return print("Aceste numere nu sunt prietene:(")

def suma_tast():
    a = int(input("Dati numarul I: "))
    b = int(input("Dati numarul II: "))
    c = a+b
    return print(a,"+",b,"=",c)

def prod_tast():
    a = int(input("Dati numarul I: "))
    b = int(input("Dati numarul II: "))
    c = a*b
    return print(a,"x",b,"=",c)

try:    
    x = int(input("Dati primul nr: "))
    y = int(input("Dati al doilea nr: "))

    print("//////////////////")
    lowest_multiple(x,y)
    print("//////////////////")
    sum(x,y)
    print("//////////////////")
    prod(x,y)
    print("//////////////////")
    media(x,y)
    print("//////////////////")
    biggest_div(x,y)
    print("//////////////////")
    max_min(x,y)
    print("//////////////////")
    common_div(x,y)
    print("//////////////////")
    common_multiple_5(x,y)
    print("//////////////////")
    common_numbers(x,y)
    print("//////////////////")
    uncommon_numbers(x,y)
    print("//////////////////")
    prietene(x,y)
    print("//////////////////")
    suma_tast()
    print("//////////////////")
    prod_tast()
except:
    print("Introduceti un numar!")




"""
Program elaborat de 
Durnea Maxim
Elev in clasa XII-a "D"
"""









