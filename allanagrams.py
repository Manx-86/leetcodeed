class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        if p_len > len(s):
            return []
        p_count = Counter(p)
        result = []
        window = Counter(s[:p_len])
        if window == p_count:
            result.append(0)
        for j in range(1, len(s) - p_len + 1):
            window[s[j - 1]] -= 1
            window[s[j + p_len - 1]] += 1
            if window == p_count:
                result.append(j)
        return result
