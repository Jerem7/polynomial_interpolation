# Jeremiasz Żołnierek-Kiełczewski
import numpy as np
import matplotlib.pyplot as plt

# walidacja
def walidacja(str_wejsciowy, typ):
    while True:
        try:
            dane_wejsciowe = input(str_wejsciowy)
            if typ == 'int':
                dane_wejsciowe = int(dane_wejsciowe)
                if dane_wejsciowe <= 0:
                    print("Liczba punktów musi być większa od zera.")
                    continue
            elif typ == 'float':
                dane_wejsciowe = float(dane_wejsciowe)
            break
        except:
            print("Niepoprawne dane wejściowe, proszę spróbować ponownie.")
    return dane_wejsciowe

# podawanie x i y
n = walidacja("Prosze wpisać ilość punktów ", "int")
wartosci_x = np.zeros(n)
wartosci_y = np.zeros(n)

for i in range(n):
    wartosci_x[i] = walidacja("wpisz wartość x dla punktu {}: ".format(i + 1), "float")
    wartosci_y[i] = walidacja("wpisz wartość y dla punktu {}: ".format(i + 1), "float")

# pobranie punktu dla ktorego ma byc interpolowane
interpolacja_dla = walidacja("Wprowadź punkt interpolacji: ", "float")

# interpolacja wielomianowa
wspolczynnik = np.polyfit(wartosci_x, wartosci_y, 2)
p = np.poly1d(wspolczynnik)
wspolczynniki = p.coefficients
p_str = ""

for i, coeff in enumerate(reversed(wspolczynniki)):
    if i == 0:
        p_str += "{}".format(round(coeff, 2))
    elif i == 1:
        p_str += " + {}x".format(round(coeff, 2))
    else:
        p_str += " + {}x^{}".format(round(coeff, 2), i)

# obliczanie wartosci interpolowanej i ekstrapolowanej
wartosc_interpolowana = p(interpolacja_dla)
wartosc_ekstrapolowana = p(wartosci_x[-1] + 1)

# pokazanie wynikow
print("Punkty:")
for i in range(n):
    print("({},{})".format(wartosci_x[i], wartosci_y[i]))
print("Wielomian aproksymujący: {}".format(p_str))
print(
    "Wartość interpolowana dla x={}: {}".format(interpolacja_dla, wartosc_interpolowana)
)
print("Wartość ekstrapolowana: {}".format(wartosc_ekstrapolowana))

# dane do wykresu
plt.plot(wartosci_x, wartosci_y, "o")
x = np.linspace(wartosci_x[0], wartosci_x[-1] + 1, 100)
plt.plot(x, p(x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolacja wielomianowa")

# dodanie punktow do wykresu
for i in range(n):
    plt.annotate(
        "({}, {})".format(wartosci_x[i], wartosci_y[i]), (wartosci_x[i], wartosci_y[i])
    )

plt.show()

input("Naciśnij dowolny klawisz, aby zamknąć program.")