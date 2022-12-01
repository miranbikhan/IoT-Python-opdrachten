word = "banaan"
x = list(word)

lines = len(word) * "_"
x_lines = list(lines)
print(lines)

gok = input("geef een letter: ")


if gok in word:
    print("contains letter")
    search = int(x.index(gok))
    print(search)
    print(x.count(gok))
    x_lines.pop(search)
    x_lines.insert(search,gok)
    print("".join(x_lines))

else:
    print("does not contain letter")
