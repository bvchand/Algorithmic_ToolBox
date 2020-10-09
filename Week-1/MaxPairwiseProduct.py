#python3
m = []
a = int(input())
n = input().split()
for i in range(a):
    m.append(n[i])
m.sort()
pro = int(m[-1]) * int(m[-2])
print(pro)




