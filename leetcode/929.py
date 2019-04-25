"""
929. Unique Email Addresses
blog : https://daimhada.tistory.com/148
problem : https://leetcode.com/problems/unique-email-addresses/
"""

class Solution:
    def numUniqueEmails(self, emails) -> int:
        email_list = set()
        for email in emails:
            email = email.split('@')
            local = ''
            for e in email[0]:
                if e == '.':
                    continue
                elif e == '+':
                    break
                else:
                    local += e
            local += '@'
            local += email[1]
            email_list.add(local)
        return len(email_list)

if __name__ == "__main__":
    s = Solution()
    string = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(string))

