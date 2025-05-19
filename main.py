
def warunki(number, txt1, txt2):
    # Use a breakpoint in the code line below to debug your script.
    if number % 2 == 0:
        print(txt2)
    else:
        print(txt1)  # Press ⌘F8 to toggle the breakpoint.


def petle(kolekcja):
    for element in kolekcja:
        print(element)

    ilosc = 10
    while ilosc > 0:
        print(ilosc)
        ilosc = ilosc - 1

    kontrola = 2
    while True:
        kontrola -= 1
        if kontrola < 0:
            break
    print('koniec')

    for i in range(5):
        pass # to jest fajne - nic nie robi ale jest instrukcja

    for i in range(6):
        if i % 2 == 0:
            continue # przeskakuje aktualne wykonanie petli
        print(i)

def listy():
    # mutowalna
    lista = ["jablko", "gruszka", "kalafior", 2] # listy mogą być mieszane - okropność :(
    print(lista[0])
    print(lista[3])
    print(lista[-1]) # elementy OD KOńCA listy - czad
    print(lista[-3])

    lista.append("na koncu")
    print(lista)
    lista.insert(1, "na wybranym miejscu")
    print(lista)
    pobrane = lista.pop(-2)
    print(pobrane)
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)


    listaNumeryczna = [1,5,3,4,6,2,8,9]
    kwadratyLiczbParzystych = [x ** 2 for x in listaNumeryczna if x % 2 == 0] # [operacja for x in lista if warunek] - buduje nową listę
    print(kwadratyLiczbParzystych)

if __name__ == '__main__':
    # warunki(2,'fajne', 'niefajne')
    # kolekcja = ["jablko", "gruszka", "zelki"]
    # petle(kolekcja)
    listy()


