from math import gcd

def inv(a, m):
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return None

def decrypt(t, a1, b1, a2, b2):
    alp = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    inv_a1 = inv(a1, m)
    inv_a2 = inv(a2, m)
    if t[0] in alp and t[1] in alp:
        res += alp[inv_a1 * (alp.index(t[0]) - b1) % m]
        res += alp[inv_a2 * (alp.index(t[1]) - b2) % m]
    else:
        return 0
    for char in t[2:]:
        if char in alp:
            a, b = a1, b1
            a1, b1 = a2, b2
            a2, b2 = ((a * a1) % m), ((b + b1) % m)
            inv_a = inv(a2, m)
            if inv_a is not None:
                res += alp[inv_a * (alp.index(char) - b2) % m]
            else:
                return 0
        else:
            return 0

    return res

def crack(c):
    for a1 in range(1, m):
        for a2 in range(1, m):
            if gcd(a1, m) != 1 or gcd(a2, m) != 1:
                continue
            for b1 in range(m):
                for b2 in range(m):
                    de_t = decrypt(c, a1, b1, a2, b2)
                    if word_count(de_t):
                        k = [a1, b1, a2, b2]
                        return de_t, k


def word_count(t):
    words = t.split()
    if len(words) == 0:
        print(0)
    for w in words:
        if w not in dictionary:
            return 0
    return 1


if __name__ == "__main__":
    m = 27
    with open("engwords.txt") as f:
        dictionary = set(w.strip() for w in f)
    c = input("Введите зашифрованный текст: ")
    print(f"Дешифрованный текст: {crack(c)[0]}")
    print(f"Выявленные ключи: a1 = {crack(c)[1][0]}, b1 = {crack(c)[1][1]}, a2 = {crack(c)[1][2]}, b2 = {crack(c)[1][3]}")