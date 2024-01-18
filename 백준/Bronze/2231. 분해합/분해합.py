N = int(input())

found = False

for i in range(N):
    tmp = i
    check = list(str(i))
    for j in range(len(check)):
        tmp += int(check[j])

    if tmp == N:
        print(i)
        found = True
        break

if not found:
    print(0)


