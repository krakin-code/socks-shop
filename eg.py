
a = int(input())
b = int(input())
if b > a:
    a, b = b, a
i = a
while i % a != 0 or i % b != 0:
    i += 1
print(i)
