multiplication = [i * j for i in range(1,3) for j in range(1,10)]
print(multiplication) 

multiplication = []
for i in range(1,3):
    for j in range(1,10):
        multiplication.append(i * j)
print(multiplication)