def produs_impar(lst):
    """
    Determina daca produsul elementelor din lista este impar.
    :param lst: o lista de numere intregi
    :return: True daca produsul elementelor este impar sau False in caz contrar
    """
    produs = 1
    for x in lst:
        produs = produs * x
    if produs % 2:
        return True
    return False


def get_longest_product_is_odd(lst):
    """
    Determina cea mai lunga subsecventa cu proprietatea ca produsul numerelor este numar impar.
    :param lst: o lista de numere intregi
    :return: cea mai lunga subsecventa continand numere a caror produs este impar
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if produs_impar(lst[i:j+1]) and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max


def concatenare_cifre_ordine_crescatoare(lst):
    """
    Verifica daca concatenarea elementelor din lista are cifrele in ordine crescatoare
    :param lst: o lista de numere intregi
    :return: True daca oridinea cifrelor este crescatoare sau False in caz contrar
    """
    ultima_cifra = 10
    for i in reversed(range(len(lst))):
        copie = lst[i]
        while copie:
            if copie % 10 > ultima_cifra:
                return False
            else:
                ultima_cifra = copie % 10
            copie = copie // 10
    return True


def get_longest_concat_digit_count_asc(lst):
    """
    Determina cea mai lunga subsecventa in care concatenarea numerelor are cifrele in ordine crescatoare.
    :param lst:  o lista de nr. intregi
    :return: cea mai lunga subsecventa continand numere a caror concatenare are cifre in ordine crescatoare
    """
    subsecventa_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if concatenare_cifre_ordine_crescatoare(lst[i:j+1]) and len(lst[i:j+1]) > len(subsecventa_max):
                subsecventa_max = lst[i:j+1]
    return subsecventa_max


def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([]) == []
    assert get_longest_product_is_odd([2, 4, 6]) == []
    assert get_longest_product_is_odd([2, 3, 4]) == [3]


def test_get_longest_concat_digit_count_asc():
    assert get_longest_concat_digit_count_asc([]) == []
    assert get_longest_concat_digit_count_asc([12, 42, 65]) == [12]
    assert get_longest_concat_digit_count_asc([4331, 7543, 1]) == [1]


def afisare_meniu():
    print("1. Citire lista")
    print("2. Determina cea mai lunga subsecventa in care produsul numerelor este numar impar.- ex. 9")
    print("3. Determina cea mai lunga subsecventa in care concatenarea nr. are cifrele in ordine crescatoare.- ex. 19")
    print("x. Iesire.")


def citire_lista():
    lst = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        lst.append(int(input("l[" + str(i) + "]=")))
    return lst


def main():
    lst = []
    while True:
        afisare_meniu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(get_longest_product_is_odd(lst))
        elif optiune == "3":
            print(get_longest_concat_digit_count_asc(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida!")


test_get_longest_product_is_odd()
test_get_longest_concat_digit_count_asc()
main()
