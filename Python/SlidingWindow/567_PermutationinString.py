class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = [0] * 26
        s2_sub_string_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_sub_string_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_sub_string_count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[left]) - ord('a')
            s2_sub_string_count[index] -= 1
            if s2_sub_string_count[index] == s1_count[index]:
                matches += 1
            if s2_sub_string_count[index] == s1_count[index] - 1:
                matches -= 1
            left += 1

            index = ord(s2[right]) - ord('a')
            s2_sub_string_count[index] += 1
            if s2_sub_string_count[index] == s1_count[index]:
                matches += 1
            if s2_sub_string_count[index] == s1_count[index] + 1:
                matches -= 1

        return matches == 26
