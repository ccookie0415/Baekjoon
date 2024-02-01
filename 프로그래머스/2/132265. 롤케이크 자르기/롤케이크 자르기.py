from collections import Counter

def solution(topping):
    n = len(topping)
    topping_set = set(topping)
    answer = 0

    left_counter = Counter()
    right_counter = Counter(topping)

    for i in range(n-1):
        left_counter[topping[i]] += 1
        right_counter[topping[i]] -= 1

        if right_counter[topping[i]] == 0:
            del right_counter[topping[i]]

        if len(left_counter) == len(right_counter):
            answer += 1

    return answer