def solution(s):
    answer = []
    dic = {}
    
    s = s.replace('{','').replace('}','').split(',')
    
    for i in s:
        if i not in dic:
            dic[i] = 1
            
        else:
            dic[i] += 1
            
    sort_dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    
    for j in sort_dic:
        answer.append(int(j[0]))
 
    return answer