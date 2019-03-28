"""
 leetcode 3. Longest Substring Without Repeating Characters (Medium)
 blog : https://daimhada.tistory.com/117
 problem : https://leetcode.com/problems/longest-substring-without-repeating-characters
"""
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        ch_dict = defaultdict(lambda : -1)
        cur_idx = 0
        length = len(s)
        cur_count = 0
        max_count = 1

        while cur_idx < length:
            ch = s[cur_idx]
            # dict에 해당 문자가 현재 체크하는 범위 내에 존재하지 않으면 (0 이하 포함)
            idx = ch_dict[ch]
            if idx == -1:
                ch_dict[ch] = cur_idx
                cur_count += 1
            else:
                max_count = max(cur_count, max_count)
                before_ch_idx = ch_dict[ch]
                # 중복된 문자열 다음부터 문자 비교를 위해 count, start_idx 수정

                start_idx = before_ch_idx + 1
                # 바로 옆과 일치하는 경우
                if before_ch_idx == (cur_idx - 1):
                    start_idx = cur_idx
                # 재 탐색 위치 수정
                cur_idx = before_ch_idx
                cur_count = 0
                ch_dict = defaultdict(lambda: -1)
                # 더이상 체크할 필요 없는 경우
                if length - start_idx <= max_count:
                    break
            cur_idx += 1
        # 마지막으로 한번 더 비교
        max_count = max(cur_count, max_count)
        return max_count


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew")) #3
print(solution.lengthOfLongestSubstring("dvdf")) #3
print(solution.lengthOfLongestSubstring("abcabcbb")) #3
print(solution.lengthOfLongestSubstring("vqblqcb")) #4
print(solution.lengthOfLongestSubstring("")) # 0
print(solution.lengthOfLongestSubstring(" ")) # 1
