L = ["Apple","Guava","Mango","Banana","Kiwi"]

print("Length of List:",len(L))

print("First Element:",L[0])
print("Last Element:",L[-1])

L.append("Papaya")
print("Updated List:",L)

L.remove("Guava")
print("Updated List:",L)

L.sort()
print("Sorted List:",L)

L.pop()
print("Updated List:",L)

L.reverse()
print("Reversed List:",L)

print("Multiplication on List:",L*2)

L = L[:4]
print("Sliced List:",L)

L.clear()
print("Updated List:",L)