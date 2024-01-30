def solution(elements):
    check = set()
    N = len(elements)
    elements = elements * 2
    
    for i in range(N):
        for j in range(N):
            check.add(sum(elements[j:j+i+1]))
            

    return len(check)