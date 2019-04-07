# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:

        start_n = 1
        result = '1'
        while start_n < n:
            cur_n = result[0]
            cnt = 1
            new_result = ''

            if len(result) == 1:
                start_n += 1
                result = '11'
                continue

            for i in range(1, len(result)):

                if cur_n != result[i]:
                    new_result += str(cnt)
                    new_result += str(cur_n)

                    # reset
                    cur_n = result[i]
                    cnt = 1
                else:
                    cnt += 1

                # last_idx
                if len(result) -1 == i:
                    new_result += str(cnt)
                    new_result += str(cur_n)
            start_n += 1
            result = new_result
        return result


s = Solution()
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(30))



