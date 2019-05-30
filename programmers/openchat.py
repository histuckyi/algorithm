
def solve(records):
    answer = []
    name_table = {}
    caseList = []
    actionList = {'Leave' : '님이 나갔습니다.', 'Enter' : '님이 들어왔습니다.'}
    for record in records:
        record = record.split(' ')
        action = record[0]
        if action != 'Leave':
            # 이름을 변경하거나 새로 생성
            name_table[record[1]] = record[2]
        if action != 'Change':
            caseList.append((action, record[1]))

    for action, id in caseList:
        answer.append(name_table[id] + actionList[action])
    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solve(record))