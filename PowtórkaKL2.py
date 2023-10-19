#ZAD1
# a = int(input())
# b = int(input())
# print((a**2)+(b**2))

# def sumakwadratów(a,b):
#   return ((a**2)+(b**2))

# print(sumakwadratów(a,b))

#ZAD2
# a = int(input())
# b = int(input())
# # print((a+b)**2)

# def kwadratsumy(a,b):
#   return ((a+b)**2)

# print(kwadratsumy(a,b))

#ZAD3
# a = int(input())
# b = int(input())
# # print((a-b)**3)

# def sześcianróznicy(a,b):
#   return (a-b)**3
# print(sześcianróznicy(a,b))

#ZAD4
# a = int(input())
# b = int(input())
# c = int(input())
# # print(a*b*c)

# def iloczyntrzechliczb(a, b, c):
#   return a*b*c
# print(iloczyntrzechliczb(a, b, c))


#ZAD5
# a = int(input())
# b = int(input())
# # print(((a+b)*2)/5)

# def dzwadziesciaprocentpodwojonejsumy(a, b):
#   return(((a+b)*2)/5)
# print(dzwadziesciaprocentpodwojonejsumy(a, b))

#ZAD6
# a = int(input())
# # print(a*0.77)

# def netto(a):
#   return(a*0.77)
# print(netto(a))

#ZAD7
# a = int(input())
# b = int(input())
# # print(a%b)

# def reszta(a, b):
#   return a%b
# print(reszta(a, b))


                       #DRUGA KARTA
#ZAD 1

# a = int(input())
# def podzielnaprzez3(a):
#   return a%3 == 0
# print(podzielnaprzez3(a))

#ZAD 2

# a = int(input())
# def jesttrzycyfripodzprzez17(a):
#   return a in range(100, 1000) and a%17 ==0
# print(jesttrzycyfripodzprzez17(a))

#ZAD3 

# wiek = int(input())
# def pełnoletni(a):
#   return a>=18
# print(pełnoletni(wiek))

#ZAD4

# waga = int(input())
# limit = 20
# def limitmostu(a):
#   return a<=limit
# print(limitmostu(waga))

# ZAD 5
# a = int(input())
# b = int(input())
# c = int(input())

# def miescisie(a, b, c):
#   return a<c<b or a>c>b
# print(miescisie(a, b, c))

#ZAD 6
# a, b = int(input()), int(input())
# def mtf(a, b):
#   return ((a**b) - a) % b ==0
# print(mtf(a, b))

#ZAD 7
# p, k, s = int(input()),int(input()),int(input())
# def skoki(a, b, c):
#   return a + 3*c >=b
# print(skoki(p, k , s))


# POWTÓRKA I KARTA

# import math
# print(math.fabs(-34))
# print("zaokrągla w dół", math.floor(34.999))
# print("zaokrągla w górę",math.ceil(34.222))

#ZAD1
# a = int(input())
# b = int(input())
# def sumajestparzysta(a, b):
#   return (a + b)%2 ==0
# print(sumajestparzysta(a, b))

#ZAD2
# import math
# a = int(input())
# g = int(input())

# def sprawdzenie(a, b):
#   return (a+b)/2 > math.sqrt((a*b))

# print(sprawdzenie(a, g))

#ZAD3 nieskończone
# a = int(input())
# b = int(input())
# c = int(input())

# def sarownea(a, b, c):
#   return (a == b and b == a and c!=a)
# def sarowneb(a, b, c):
#   return (a == b and b == a and c!=a)
# def sarownec(a, b, c):
#   return (a == b and b == a and c!=a)
# def sarowneal(a, b, c):
#   return (a == b and b == a and c!=a)
# print(sarowne(a, b, c))

#ZAD4
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# def jestnajmniej(a, b, c, d):
#   list = [a, b, c, d]
#   return min(list)
# print(jestnajmniej(a, b, c, d))





#KARTA PRACY3
#ZAD1
# n = int(input())
# def szesz(a):
#   for petla in range(0, a+1):
#     petla = (petla**3)+3
#     print(petla)
# print(szesz(n))

#ZAD2
# def szesz():
#   for petla in range(105, 1000, 15):
#     print(petla)
    
# print(szesz())

#ZAD3
# n = int(input())
# def dziel(n):
#   for i in range(1, n+1):
#     if n%i ==0:
#       print(i)
# print(dziel(n))

#ZAD4
# def sum():
#   suma = 0
#   for i in range(10, 100):
#     suma = suma + i
#   print(suma)
      
# print(sum())

#ZAD5


#                KARTA 3A
#TABLICA (nwm co się dzieje, tablica jest zmieniona)

# size = int(input())
# for i in range(size):
#   for j in range(size):
#     if i == j:
#       print("*", end="")
#     else:
#       print(" ", end="")
# print()


#ZAD7
# size = int(input())
# for i in range(size):
#   for j in range(size):
#     if i == 0 or i == size-1 or j == 0 or j == size-1 or i==j==size//2:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

#ZAD5
# size = int(input())
# for i in range(size):
#   for j in range(size):
#     if j==size//2:
#       print("*", end="")
#     elif i==size//2:
#       print("-", end="")
#     else:
#       print(" ", end="")
#   print()

#ZAD4
# size = int(input())
# for i in range(size):
#   for j in range(size):
#     if j+i ==size//2 or j-i ==size//2 or i-j ==size//2 or j+i ==3*size//2:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()


#TABLICO LISTY
# list = [3, 4, 5, 6, 7, 8, 2, 6, 3]
# print(list)

# import random
# list = []
# list = random.sample(range(0, 50), 10)

## TO TO SAMO CO:

# for i in range(10):
#   list.append(random.randint(0, 50))


# SORTOWANIE BĄBELKOWE

# import random
# list = []
# list = random.sample(range(0, 50), 10)

# n = len(list)
# print(list)
# for i in range(n-1):
#   for j in range(n-1):
#     if list[j] > list[j+1]:
#       list[j], list[j+1] = list[j+1], list[j]
    
# print("posortowane:\n", list)

# KARTA 3B
#ZAD1
# def paź():
#   list = []
#   for i in range(1, 31):
#     list.append(i)
#   print(list)
# print(paź())

#ZAD2

# def kwadr():
#   list = []
#   for i in range(1, 10):
#     list.append(i**2)
#   print(list)
# print(kwadr())

#ZAD3

# def dzieli():
#   list = []
#   for i in range(1000, 10000):
#     if i%379 ==0:
#       list.append(i)
#   print(list)
# print(dzieli())



 #SORTOWANIE BĄBELKOWE
# import random
# list = []
# list = random.sample(range(0, 50), 10)
# n = len(list)

# for i in range(n-1):
#   for j in range(n-1):
#     if list[j] > list[j+1]:
#       list[j], list[j+1] = list[j+1], list[j]

# print("posortowane:", list)

# TABLICZKA MNOŻENIA

# for x in range(1,11):
#  for y in range(1,11):
#      print (x*y, end="   ")
#  print()

#ZAD4

# def dzieli():
#   list = []
#   for i in range(100, 1000):
#     if (i%6 ==0 and i%5==0) or (i%6 ==0 and i%5==0 and i%11 ==0):
#       list.append(i)
#   print(list)
# print(dzieli())

#ZAD5


# def sumawpetli():
#   a = int(input())
#   suma = 0
#   for i in range(a):
#     b = int(input())
#     suma += b
#   print(suma)
# print(sumawpetli())

        #REKURENCJA

# a = int(input())
# def f(a):
#   if (a==0):
#     return 3
#   else:
#     return f(a-1)+2
# print(f(a))

p = int(input())
w = int(input())
def potego(p, w):
  if (p==0):
    return 1
  else:
    return 
print(potego(p, w))