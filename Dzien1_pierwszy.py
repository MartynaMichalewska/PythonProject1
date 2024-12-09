import sys
import decimal

print("radek")
print(39)
print(sys.int_info)
# print("30"+40) sam nie zamienia typow
a=decimal.Decimal("10")
print(a)

a=decimal.Decimal("2.3456")
b=decimal.Decimal("3.1234")
print(a+b)
precyzja=decimal.Decimal("0.00")
print((a+b).quantize(precyzja))
#typ logiczny
#True False
# ctr + d - kopiowanie linijki
print(int(True)) # 1
print(int(False)) # 0
print(bool(1)) #True
print(bool(100)) #True
print(bool(230)) #True
print(bool(None)) #True
print(None) #True
tekst="ola"
print(tekst.upper())

# kolekcja - zapamietuje wiele elementow, rozne typy na raz
# lista, krotka (tuple), zbior (set), slownik, dict)
# krotka - lista do odczytu, nic w niej nei moze zmienic, najefektywniejszy typ danych
# zbior - unikalne wartosci
# slownik - para: klucz + wartosc

# lista
lista=[2,3,4,5,6]
lista2=lista
lista.clear()
print(lista2) # lista2 tez bedzie pusta
lista=[2,3,4,5,6]
lista3=lista.copy()
lista.clear()
print(lista3) # lista3 nie bedzie pusta

krotka=tuple(lista3)
print(krotka) # (2, 3, 4, 5, 6)

zbior= {2,2,3,4,5,5,5,5,5}
print(zbior) # {2, 3, 4, 5}

slownik={ "name":"radek","age":45}
print(slownik)

print("www")





