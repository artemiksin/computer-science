from math import sqrt
from time import time

def time_to_do(x):
  start = time()
  x()
  end = time()
  return (end - start)


def decorate(x):
  print('Start function' + x.__name__)
  print("Run time: {:.2f}".format(time_to_do(x)))

  


def Task1():
    a = int(input('Width: '))
    b = int(input('Height: '))
    SQFT_PER_ACRE = a*b
    print("Square: {:.2f}".format(float(SQFT_PER_ACRE)/43560))

def Task2():
    a = 9.8
    d = float(input("Height: "))
    v0 = 0.0
    v = sqrt(v0)**(1/2) + 2*a*d
    print("Square: {:.2f}".format(v))

decorate(Task1)
decorate(Task2)