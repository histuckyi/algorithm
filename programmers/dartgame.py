
"""
    (2017) KAKAO BLIND RECRUITMENT 
    [1차] 다트 게임
    https://programmers.co.kr/learn/courses/30/lessons/17682

    solution.
    입력받은 문자열을 조건에 따라 문자 단위로 나누고 원하는 값을 도출하는 문제다.
    입력받은 다트의 점수가 10점일 때와 0점일 때만 잘 처리해주면 된다.
    처음에는 문자가 숫자일 경우에 리스트에 값을 채워 넣고,
    index 값을 저장하여 처리를 해줘야하는 다트의 점수를 찾아 조건대로 후처리해주는 방식이었으나,
    그럴 경우 10점일 때의 처리가 이뤄지지 않으므로 그 부분을 아래의 코드처럼
    나누어 처리해줘야 한다.
"""

def solution(dartResult):
    records = []
    last_record_idx = None
    dart_length = len(dartResult)
    dart_last_index = dart_length - 1
    for i in range(dart_length):
        value = dartResult[i]

        if value.isdigit():
            # number is 10, if char is 1, check next character
            if i < dart_last_index - 1 and dartResult[i + 1].isdigit():
                    value += dartResult[i + 1]
            # number is 10, if char is 0, check before character
            if value == '0' and i > 0 and dartResult[i -1].isdigit():
                continue
            records.append(int(value))
            last_record_idx = len(records) - 1
        else:
            if value == "D":
                records[last_record_idx] **= 2
            elif value == "T":
                records[last_record_idx] **= 3
            elif value == "*":
                if last_record_idx != 0:
                    records[last_record_idx -1] *= 2
                records[last_record_idx] *= 2
            elif value == "#":
                records[last_record_idx] = (-records[last_record_idx])
    return sum(records)

if __name__ == "__main__":

    print(solution('1S2D*3T')) # 37
    print(solution('1D2S#10S')) # 9
    print(solution('1D2S0T')) # 3
    print(solution('1S*2T*3S')) # 23
    print(solution('1D#2S*3S')) # 5
    print(solution('1T2D3D#')) # -4
    print(solution('1D2S3T*')) # 59
