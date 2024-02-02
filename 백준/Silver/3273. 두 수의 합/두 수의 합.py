n = int(input())
numbers = list(map(int,input().split()))
target = int(input())
answer = 0
numbers.sort()
front_pointer = 0
back_pointer = len(numbers)-1

while True:
    if front_pointer == back_pointer:
        break

    if numbers[front_pointer] + numbers[back_pointer] == target:
        answer += 1
        back_pointer -= 1

    elif numbers[front_pointer] + numbers[back_pointer] > target:
        back_pointer -= 1

    else:
        front_pointer += 1

print(answer)

