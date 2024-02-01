def solution(record):
    answer = []
    name = {}
    
    for i in range(len(record)):
        record[i] = record[i].split()
        
        if record[i][0] == 'Enter':
            name[record[i][1]] = record[i][2]
            answer.append([f'{record[i][1]} 님이 들어왔습니다.'])
            
        elif record[i][0] == 'Change':
            name[record[i][1]] = record[i][2]
        
        else:
            answer.append([f'{record[i][1]} 님이 나갔습니다.'])
        
    for j in range(len(answer)):
        answer[j] = answer[j][0].split()
        answer[j][0] = name[answer[j][0]]
        answer[j] = answer[j][0] + answer[j][1] + ' ' + answer[j][2]
        
    
    return answer