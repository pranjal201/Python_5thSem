# ternary operator are use to evaluate a condition in a single line

a, b = 10, 20

min = a if a < b else b

print(min)

print((b, a)[a > b])

print({True: a, False: b} [a > b])

print(100**100)
