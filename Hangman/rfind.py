word = "banaan"

lines = len(word) * "_"
x_lines = list(lines)
print(lines)

gok = input("geef een letter: ")


for gok in word:
    while True:
        print("contains letter")
        search = word.rfind(gok)
        print(search)
        print(word.count(gok))
        x_lines.pop(search)
        x_lines.insert(search,gok)
        print("".join(x_lines))
        break
else:
    print("where letter?")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x) 


# txt = "Mi casa, su casa."
# x = txt.rfind("casa")
# print(x)


# while gok in word:
#     print("contains letter")
#     search = int(x.count(gok))
#     print(search)
#     print(x.count(gok))
#     x_lines.pop(search)
#     x_lines.insert(search,gok)
#     break