class Solution(object):
    def myAtoi(self, text):
        text = text.strip()
        if not text:
            return 0
        idx = 0
        multiplier = 1
        value = 0
        if text[idx] == '-' or text[idx] == '+':
            multiplier = -1 if text[idx] == '-' else 1
            idx += 1
        while idx < len(text) and text[idx].isdigit():
            num = int(text[idx])
            if value > (2**31 - 1 - num) // 10:
                return 2**31 - 1 if multiplier == 1 else -2**31
            value = value * 10 + num
            idx += 1
        return multiplier * value
