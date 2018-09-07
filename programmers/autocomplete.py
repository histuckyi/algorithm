"""
    (2017) KAKAO BLIND RECRUITMENT 
    [3차] 자동완성
    https://programmers.co.kr/learn/courses/30/lessons/17685

    solution.
    1. 단어 리스트를 정렬한다.
    2. 정렬한 단어 리스트에서 단어를 하나씩 뽑아, 해당 단어의 앞,뒤 단어와 비교하여 일치하는 글자까지의 index를 알아낸다.
    3. 이때, 단어 리스트의 맨 앞과 맨 뒤의 단어의 경우를 예외처리해줘야 한다.
        맨 앞 단어는 그 앞에 단어가 없으므로 체크해선 안되며,
        맨 뒤 단어도 그 뒤에 단어가 없으므로 체크할 수 없다.
    4. 앞, 뒤 단어와 모두 일치하지 않는 경우(front_idx, back_idx == -1) 한글자만 입력하면 되고,
       둘 중 일치하는 index가 가장 큰 수 만큼 입력해야 하되,
       단어 전체 길이만큼 일치한는 경우는 단어의 길이만큼 입력해야 하고,
       단어 전체 길이보다 적은 수만큼 일치하는 경우, 그 다음 단어까지 입력해야하므로 +1을 더 해주어야 한다.
"""

def solution(words):
    word_cnt = 0 # total word count
    words.sort() # sorting

    for word_idx in range(len(words)):
        current_word = words[word_idx] #  word to look for
        current_word_length = len(current_word)
        current_word_last_index = current_word_length -1  # length -> last index
        front_idx = -1 # Index matching with previous word
        back_idx = -1 # Index matching with back word

        # idx == 0 -> pass
        if word_idx > 0:
            front_word = words[word_idx -1]
            for i in range(current_word_length):
                if i == len(front_word):
                    break
                if front_word[i] == current_word[i]:
                    front_idx += 1
                else:
                    break

        # idx == last index -> pass
        if word_idx < len(words) - 1:
            back_word = words[word_idx +1]
            for j in range(current_word_length):
                if j == len(back_word):
                    break
                if back_word[j] == current_word[j]:
                    back_idx += 1
                else:
                    break

        # both front,back word do not match the current word -> 1 character
        if front_idx == -1 and back_idx == -1:
            word_cnt += 1
        else:
            max_idx = max(front_idx, back_idx)
            max_cnt = max_idx + 1 # idex -> length
            # @warning, if more than word length, one more character. (index + 1) + 1 
            if max_idx < current_word_last_index:
                max_cnt += 1
            word_cnt += max_cnt  
    return word_cnt

if __name__=="__main__":
    print(solution(['go','gone','guild']))  # result : 7
    print(solution(['abc','def','ghi','jklm'])) # result : 4
    print(solution(['word','war','warrior','world'])) # result : 15
                




            


