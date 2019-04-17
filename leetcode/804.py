"""
LeetCode. 804. Unique Morse Code Words
blog : https://daimhada.tistory.com/140
problem: https://leetcode.com/problems/unique-morse-code-words/
"""

class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        """
        fater than 97.87% of Python3
        Memory Usage : less than 5.36% of Python3

        ord('a') # 97
        ord('z') # 122
        """
        alpha_dict = {}
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",\
                      ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", \
                      ".--", "-..-", "-.--", "--.."]
        for i in range(ord('a'), ord('z') + 1):

            alpha_dict[chr(i)] = morse_code[i-ord('a')]

        changed_words = set()
        for word in words:
            string = ''
            for c in word:
                string += alpha_dict[c]
            if string not in changed_words:
                changed_words.add(string)

        return len(changed_words)


if __name__ == "__main__":
    s = Solution()
    word = ["gin", "zen", "gig", "msg"]
    print(s.uniqueMorseRepresentations(word))