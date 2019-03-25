"""
LeetCode 551. Student Attendance Record I
blog : https://daimhada.tistory.com/115
problem : https://leetcode.com/problems/student-attendance-record-i
"""

class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        for i in range(len(s)):
            ch = s[i]
            if ch == 'A':
                a_count += 1
                if 1 < a_count:
                    return False
            elif ch == 'L':
                if i+1 < len(s) and i+2 < len(s):
                    if s[i+1] == 'L' and s[i+2] == 'L':
                        return False
        return True