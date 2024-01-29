def solution(id_list, report, k):
    answer = []
    dic = {}
    report_list = [0 for _ in range(len(id_list))]
    report_people = []
    check_list = {}
    
    for id in id_list:
        dic[id] = [0,[],0]
        check_list[id] = 0

    for repo in report:
        
        if repo.split()[1] not in dic[repo.split()[0]][1]:
            dic[repo.split()[0]][1].append(repo.split()[1])
            dic[repo.split()[1]][0] += 1
    
    for key,values in dic.items():
        if values[0] >= k:
            report_people.append(key)
    
    for name in report_people:
        for key,values in dic.items():
            if name in values[1]:
                values[2] += 1
    
    for key,values in dic.items():
        answer.append(values[2])
    
    return answer