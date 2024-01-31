def solution(progresses, speeds):
    answer = []
    
    while True:
        if not progresses:
            break
            
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        if progresses[0] >= 100:
            tmp = 0
            while progresses:
                if progresses[0] < 100:
                    break
                    
                else:
                    progresses.pop(0)
                    speeds.pop(0)
                    tmp += 1
                    
            answer.append(tmp)
                    
            
                
    
    return answer