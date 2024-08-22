class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t, count_s = {}, {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        left = 0
        for right in range(len(s)):
            if s[right] in count_t:
                count_s[s[right]] = count_s.get(s[right], 0) + 1
                if count_s[s[right]] == count_t[s[right]]:
                    have += 1

            while have == need:
                current_length = right - left + 1
                if current_length < res_len:
                    res = [left, right + 1]
                    res_len = current_length

                if s[left] in count_t:
                    count_s[s[left]] -= 1
                    if count_s[s[left]] < count_t[s[left]]:
                        have -= 1
                left += 1
        return s[res[0]:res[1]] if res_len != float("inf") else ""
