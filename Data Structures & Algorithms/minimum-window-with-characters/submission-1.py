class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        have, need = 0, len(countT)
        l = 0
        answer = [0, 0]
        length = float("inf")
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    length = (r - l + 1)
                    answer[0] = l
                    answer[1] = r
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        if length == float("inf"):
            return ""
        return s[answer[0]:answer[1]+1]