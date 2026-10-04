class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = dict()
        t_chars = dict()

        for i in range(len(s)):
            if s[i] not in s_chars:
                s_chars[s[i]] = 0
            if t[i] not in t_chars:
                t_chars[t[i]] = 0
            s_chars[s[i]] += 1
            t_chars[t[i]] += 1

        return s_chars == t_chars