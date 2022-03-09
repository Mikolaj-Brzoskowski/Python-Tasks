from math import sqrt 
from random import randrange
from statistics import mean

def zad2_a(tab1, tab2):
    sum = []
    product = []
    for i in range(0, len(tab1)):
        sum.append(tab1[i] + tab2[i])
        product.append(tab1[i] * tab2[i])
    return (sum, product)

print(zad2_a([3, 8, 9, 10, 12], [8, 7, 7, 5, 6]))

def zad2_b(tab1, tab2):
    prod = []
    for i in range(0, len(tab1)):
        prod.append(tab1[i] * tab2[i])
    return sum(prod)

print(zad2_b([3, 8, 9, 10, 12], [8, 7, 7, 5, 6]))

def zad2_c(vector):
    result = 0
    for item in vector:
        result += item ** 2
    return sqrt(result)

print(zad2_c([3, 8, 9, 10, 12]))
print(zad2_c([8, 7, 7, 5, 6]))

def zad2_d():
    result = []
    for i in range(0, 50):
        result.append(randrange(1,101))
    return result

vector = zad2_d()
print(vector)

def zad2_e(vec):
    minimum = min(vec)
    maximum = max(vec)
    mean_var = mean(vec)
    sd = 0
    for item in vec:
        sd += (item - mean_var) ** 2
    sd = sqrt(sd/len(vec))
    return (minimum, maximum, mean_var, sd)

print(zad2_e(vector))

def zad2_f(vec):
    result = []
    minimum = min(vec)
    maximum = max(vec)
    for item in vec:
        result.append((item - minimum)/(maximum - minimum))
    return result

print(zad2_f(vector))

