# -*- coding: utf-8 -*-
"""лаба№3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RvmA3SSh7uFHqex4USSAZfzJEP0qWKpa
"""

month = int(input())
if month == 1:
  print("Январь")
elif month == 2:
  print("Февраль")
elif month == 3:
  print("Март")
elif month == 4:
  print("Апрель")
elif month == 5:
  print("Май")
elif month == 6:
  print("Июнь")
elif month == 7:
  print("Июль")
elif month == 8:
  print("Август")
elif month == 9:
  print("Сентябрь")
elif month == 10:
  print("Октябрь")
elif month == 11:
  print("Ноябрь")
elif month == 12:
  print("Декабрь")

a = int(input())
if a%2 == 0:
  print("chOtnoE")

N = int(input())
if N>40:
  print("stonks")
elif N<40:
  print("not stonks")

def is_year():
  year=int(input())
  if year%4==0 and(year%100!=0 or year%400==0):
    print(True)
  else: print(False)
is_year()

def is_prime():
  n=int(input())
  if n>1 and n%n==1 and n%1==n:
    print(True)
  else: print(False)
is_prime()

p = int(input())
def is_prime(n):
  s=2
  while n%s!=0:
    s+=1
  return s==n

print(is_prime(p))
if(is_prime(p)):
  print("простое")
else:
  print("сложное")

import math
num1 = float(input())
num2 = float(input())
n1 = (-138/2)**1.3
n2 = math.fabs((-69/(28**5.1))*4)
aogr1 = n1.real
bogr1 = n1.imag
realn1 = -1*(aogr1**2 + bogr1**2)**0.5
print("До проверки для обмена значений: ", "\n  num1 = ", num1, "\n  num2 = ", num2)
if(num1 > 3.6*num2) or (num2 >= realn1 and num2 <= n2):
  num1, num2 = num2, num1
print("После проверки для обмена значений: ", "\n  num1 = ", num1, "\n  num2 = ", num2)