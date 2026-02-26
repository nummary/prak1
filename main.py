import math

def inv(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    else:
        return None

def zamena(t, ed):
    alp = input("Введите алфавит: ")
    k = input("Введите ключ: ")
    if len(alp) != len(k):
        return "ОШИБКА: Неверный ключ"
    res = ""
    if ed == 1:
        for char in t:
            if char not in alp:
                return f"ОШИБКА: Символа '{char}' нет в алфавите"
            res += k[alp.index(char)]
    elif ed == 2:
        for char in t:
            if char not in alp:
                return f"ОШИБКА: Символа '{char}' нет в алфавите"
            res += alp[k.index(char)]
    else:
        return "ОШИБКА: Неверный режим"

    return res


def affine(t, ed):
    alp = input("Введите алфавит или 1 для английского: ")
    if alp == "1":
        alp = alphabet
    a, b = map(int, input("Введите ключ(a b): ").split())
    m = len(alp)
    if math.gcd(a, m) != 1:
        return "ОШИБКА: Неверный ключ"
    res = ""
    if ed == 1:
        for char in t:
            if char in alp:
                res += alp[(alp.index(char) * a + b) % m]
            else:
                return f"ОШИБКА: Символа '{char}' нет в алфавите"
    elif ed == 2:
        inv_a = inv(a, m)
        if inv_a is not None:
            for char in t:
                if char in alp:
                    res += alp[(inv_a*(alp.index(char) - b)) % m]
                else:
                    return f"ОШИБКА: Символа '{char}' нет в алфавите"

        else:
            return "ОШИБКА: Невозможно расшифровать"
    else:
        return "ОШИБКА: Неверный режим"

    return res


def affine_rec(t, ed):
    alp = input("Введите алфавит или 1 для английского: ")
    if alp == "1":
        alp = alphabet
    a1, b1 = map(int, input("Введите ключ1(a b): ").split())
    a2, b2 = map(int, input("Введите ключ2(a b): ").split())
    m = len(alp)
    if math.gcd(a1, m) != 1 or math.gcd(a2, m) != 1:
        return "ОШИБКА: Неверный ключ"
    res = ""
    if ed == 1:
        if t[0] in alp and t[1] in alp:
            res += alp[(alp.index(t[0]) * a1 + b1) % m]
            res += alp[(alp.index(t[1]) * a2 + b2) % m]
        else:
            return f"ОШИБКА: Символа нет в алфавите"
        for char in t[2:]:
            if char in alp:
                a, b = a1, b1
                a1, b1 = a2, b2
                a2, b2 = ((a * a1) % m), ((b + b1) % m)
                res += alp[(alp.index(char) * a2 + b2) % m]
            else:
                return f"ОШИБКА: Символа '{char}' нет в алфавите"
    elif ed == 2:
        inv_a1 = inv(a1, m)
        inv_a2 = inv(a2, m)
        if inv_a1 is not None and inv_a2 is not None:
            if t[0] in alp and t[1] in alp:
                res += alp[inv_a1 * (alp.index(t[0]) - b1) % m]
                res += alp[inv_a2 * (alp.index(t[1]) - b2) % m]
            else:
                return f"ОШИБКА: Символа нет в алфавите"
        else:
            return "ОШИБКА: Неверный ключ"
        for char in t[2:]:
            if char in alp:
                a, b = a1, b1
                a1, b1 = a2, b2
                a2, b2 = ((a * a1) % m), ((b + b1) % m)
                inv_a = inv(a2, m)
                if inv_a is not None:
                    res += alp[inv_a * (alp.index(char) - b2) % m]
                else:
                    return "ОШИБКА: Невозможно расшифровать"
            else:
                return f"ОШИБКА: Символа '{char}' нет в алфавите"

    else:
        return "ОШИБКА: Неверный режим"

    return res


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    print("1) Простая замена")
    print("2) Аффинный")
    print("3) Аффинный рекуррентный")
    choice = int(input("Выберите шифр: "))
    text = input("Введите текст (более 2 символов): ")
    if len(text) <= 2:
        print("Текст слишком короткий")
        exit()
    print("1) Зашифровать")
    print("2) Расшифровать")
    enc_dec = int(input("Выберите: "))
    if choice == 1:
        print(zamena(text, enc_dec))
    elif choice == 2:
        print(affine(text, enc_dec))
    elif choice == 3:
        print(affine_rec(text, enc_dec))
    else:
        print("Ошибка ввода")
