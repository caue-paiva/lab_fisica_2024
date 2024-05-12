import math

n = int(input())

x_lista = []
y_lista = []

for i in range(n):
    x = float(input().replace(",", "."))

    x_lista.append(x)

for i in range(n):
    y = float(input().replace(",", "."))

    y_lista.append(y)

#x média
x_media = sum(x_lista) / len(x_lista)

#y média
y_media =  sum(y_lista) / len(y_lista)

#x²
x_ao_2 = []

for i in range(n):
    x_ao_2.append(x_lista[i] ** 2)

#xi - x_media
xi_menos_x_media = []

for i in range(n):
    xi_menos_x_media.append(x_lista[i] - x_media)

#(xi - x_media)²
xi_menos_x_media_ao_2 = []

for i in range(n):
    xi_menos_x_media_ao_2.append(xi_menos_x_media[i] ** 2)

#(xi - x_media) * yi
xi_menos_x_media_x_yi = []
for i in range(n):
    xi_menos_x_media_x_yi.append(xi_menos_x_media[i] * y_lista[i])

#calculo do a
a = sum(xi_menos_x_media_x_yi) / sum(xi_menos_x_media_ao_2)

#calculo do b
b = y_media - (a*x_media)

#calculo do Yc
yc_lista = []

for i in range(n):
    yc_lista.append((a * x_lista[i]) + b)

#(yci - yi)²
yci_menos_yi_ao_2 = []

for i in range(n):
    yci_menos_yi_ao_2.append((yc_lista[i] - y_lista[i])**2)

#calculo do deltay
delta_y = math.sqrt(sum(yci_menos_yi_ao_2) / (n - 2))

#delta a
delta_a = delta_y / (math.sqrt(sum(xi_menos_x_media_ao_2)))

#delta b
delta_b = delta_y * math.sqrt(sum(x_ao_2) / (n * sum(xi_menos_x_media_ao_2)))

#printar
print("Xi: ", x_lista)
print("Xi²: ", x_ao_2)

print("Yi: ", y_lista)

print("Xi - xmedia: ", xi_menos_x_media)
print("(xi - xmedia)²: ", xi_menos_x_media_ao_2)
print("(xi - xmedia)yi: ", xi_menos_x_media_x_yi)

print("Yci: ", yc_lista)
print("(Yci - Yi)²: ", yci_menos_yi_ao_2)

print()

print("a: ", a)
print("Delta a: ", delta_a)

print()

print("b: ", b)
print("Delta b: ", delta_b)