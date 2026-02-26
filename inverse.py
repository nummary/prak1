import math as m
while 1:
	a = int(input())
	for i in range(1, 26):
		if (a*i)%26 == 1:
			print(f"={i}")
			break
