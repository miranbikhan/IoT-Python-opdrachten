# lst = ['maart', 'februari', 'mei']
# print(lst[0])

word = "banaan"

lines = len(word) * "_"
x_lines = list(lines)
print(x_lines)
print(lines)


x = list(word)

# for index, x in enumerate(word):
#     print(index, x)

gok = input("geef een letter: ")


if gok in word:
    print("contains letter")
    search = word.index(gok)
    print(search)
    print(word.count(gok))
else:
    print("does not contain letter")

