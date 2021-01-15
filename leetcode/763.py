"""
LeetCode : 763. Partition Labels
problem : https://leetcode.com/problems/partition-labels/
"""


class Solution:

    @staticmethod
    def partitionLabels(self, s):
        s = list(s)
        # key : char, value (first_idx, last_idx)
        last_idx_dic = {}
        result = []
        idx = 0
        for char in s:
            if char in last_idx_dic:
                last_idx_dic[char] = idx
            else:
                last_idx_dic[char] = idx
            idx += 1

        cur_idx = -1
        while cur_idx != len(s) - 1:
            cur_idx += 1
            #  첫 단어 추출
            word_start_idx = cur_idx
            c = s[cur_idx]
            last_idx = last_idx_dic[c]
            # 사이에 들어있는 char들 검증 시작
            while cur_idx != last_idx:
                c = s[cur_idx]
                if last_idx <= last_idx_dic[c]:
                    last_idx = last_idx_dic[c]
                cur_idx += 1
            # result.append("".join(s[word_start_idx:last_idx + 1]))
            result.append(last_idx - word_start_idx + 1)

        return result











if __name__ == "__main__":
    st = "ababcbacadefegdehijhklij"  # [9,7,8]
    # st = "abac"  # [9,7,8]
    s = Solution()
    print(s.partitionLabels(st))