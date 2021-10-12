def is_palindrome(n):
    """
    determina daca n e palindrom
    :param n: nr. intreg
    :return: true daca n e palindrom,iar false in caz contrar
    """
    cn = n
    pal = 0
    while cn != 0:
        pal = pal * 10 + cn % 10
        cn = cn // 10
    if (n == pal):
        return True
    else:
        return False
def test_is_palindrome():
    assert is_palindrome(12) is False
    assert is_palindrome(100) is False
    assert is_palindrome(121) is True
    assert is_palindrome(1331) is True
    assert is_palindrome(1) is True
def all_palindrome(lst):
    '''
    Determina daca toate numerele dintr-o lista sunt palindrom.
    :param lst: Lista de numere intregi.
    :return: True, daca toate numerele din l sunt palindrom sau False, in caz contrar.
    '''
    for x in lst:
        if not is_palindrome(x):
            return False
    return True
def test_all_palindrome():
    assert all_palindrome([1]) is True
    assert all_palindrome([11, 414, 525]) is True
    assert all_palindrome([10, 20]) is False
    assert all_palindrome([3, 5, 7]) is True
    assert all_palindrome([111, 100, 121]) is False


def is_prime(n):
    """
    Determina daca un numar dat este prim
    :param n: nr. intreg
    :return: True daca acesta este numar prim, False in caz contrar
    """
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True
def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(12) is False
    assert is_prime(11) is True
def all_prime_digits(lst):
    """
    Determina daca toate numerele dintr-o lista sunt numere a caror cifre sunt prime.
    :param lst: lista de nr. intregi
    :return: True, daca toate nr. in lista au cifre prime, False in caz contrar.
    """
    for x in lst:
        while x != 0:
            if not is_prime( x % 10):
                return False
            x = x // 10
    return True
def test_allPrimeDigits():
    assert all_prime_digits([]) is True
    assert all_prime_digits([5, 7, 12]) is False
    assert all_prime_digits([23, 37, 53]) is True
    assert all_prime_digits([1, 101, 204]) is False
    assert all_prime_digits([3, 5, 7]) is True


def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga subsecventa in care toate elementele sunt palindrom.
    :param lst: o lista de numere intregi
    :return: cea mai lunga subsecventa in care toate elementele sunt palindrom
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_palindrome(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result):
                result = lst[i:j+1]
    return result
def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([45, 122, 121, 252]) == [121, 252]
    assert get_longest_all_palindromes([154, 75, 100]) == []
    assert get_longest_all_palindromes([111, 154, 12521, 5, 171]) == [12521, 5, 171]
    assert get_longest_all_palindromes([2, 8, 10]) == [2,8]
    assert get_longest_all_palindromes([12, 17, 22]) == [22]


def get_longest_prime_digits(lst: list[int]) -> list[int]:
    """
    Determina cea mai lunga subsecventa in care toate nr. au cifrele prime.
    :param lst: lista de numere intregi
    :return: cea mai lunga subsecventa in care toate nr. au cifrele prime
    """
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_prime_digits(lst[i:j+1]) and len(lst[i:j+1]) > len(result):
                result = lst[i:j+1]
    return result
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([1, 3, 7]) == [3, 7]
    assert get_longest_prime_digits([2, 5, 7, 11]) == [2, 5, 7]
    assert get_longest_prime_digits([2, 8, 10, 27, 33, 36]) == [27, 33]
    assert get_longest_prime_digits([10, 20, 101, 257]) == [257]


def all_tests():
    test_is_palindrome()
    test_all_palindrome()
    test_is_prime()
    test_allPrimeDigits()
    test_get_longest_all_palindromes()
    test_get_longest_prime_digits()


def citire_lista():
    list = []
    list_string = input("Dati lista, cu elementele separate prin spatiu: ")
    list_string_split = list_string.split(" ")
    for x in list_string_split:
        list.append(int(x))
    return list


def print_Menu():
    print("1. Citire date.")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea ca toate elementele sunt palindrom")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea ca toate nr. au cifrele prime")
    print("4. Iesire")

def main():
    all_tests()
    while True:
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            list = []
            list = citire_lista()
        elif optiune == "2":
            print(get_longest_all_palindromes(list))
        elif optiune == "3":
            print(get_longest_prime_digits(list))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita. Incercati din nou.")


if __name__ == '__main__':
    main()