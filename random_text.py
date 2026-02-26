from random import randint
with open("engwords.txt") as f:
	dct = [w.strip() for w in f]
k = int(input("Введите количество слов: "))
l = []
for i in range(k):
	l.append(dct[randint(0, len(dct))])
print(' '.join(l))