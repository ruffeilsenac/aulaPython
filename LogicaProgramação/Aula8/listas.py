frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
print(frutas[1])
frutas[1] = "morango"
print(frutas[1])

frutas.append("açai")
print(frutas)

frutas.insert(2, "kiwi")
print(frutas)

frutas.pop()
print(frutas)

frutas.pop(2)
print(frutas)

frutas.remove("uva")
print(frutas)

frutas.sort()
print(frutas)

print(len(frutas))

