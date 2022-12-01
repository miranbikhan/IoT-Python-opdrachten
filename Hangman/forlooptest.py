word = "banaan"

lines = len(word) * "_"
x_lines = list(lines)
print(lines)

gok = input("geef een letter: ")

search = word.rfind(gok)


while gok in word:
    print("contains letter")
    print(search)
    print(word.count(gok))
    x_lines.pop(search)
    x_lines.insert(search,gok)
    break
print("".join(x_lines))

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