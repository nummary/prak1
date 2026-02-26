t = input()
# d = {}
# for i in t:
# 	try:
# 		d[i] += 1
# 	except:
# 		d[i] = 1
# d = dict(sorted(d.items(), key=lambda item: item[1]))
# for i in d:
# 	print(i, d[i])

r = ""
for i in t:
	if i == "m": r+=" "
	elif i == "t": r+="e"
	elif i == "z": r+="t"
	elif i == "g": r+="o"
	elif i == "i": r+="h"
	elif i == "k": r+="r"
	elif i == "l": r+="s"
	elif i == "e": r+="c"
	elif i == "o": r+="i"
	elif i == "h": r+="p"
	elif i == "b": r+="y"
	elif i == "d": r+="m"
	elif i == "u": r+="g"
	elif i == "q": r+="a"
	elif i == "f": r+="n"
	elif i == "y": r+="f"
	elif i == "s": r+="l"
	elif i == "r": r+="d"
	elif i == "w": r+="b"
	elif i == "a": r+="k"
	elif i == "x": r+="u"
	elif i == " ": r+="x"
	elif i == "v": r+="w"
	elif i == "n": r+="s"
	elif i == "c": r+="v"
	elif i == "j": r+="q"
	else:r+="++++"
print(r)
