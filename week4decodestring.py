class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch != ']':
                stk.append(ch)
            else:
                segment = ''
                while stk[-1] != '[':
                    segment += stk.pop()
                stk.pop()
                num_str = ''
                while stk and stk[-1].isdigit():
                    num_str += stk.pop()
                stk.append(segment * int(num_str[::-1]))
        return ''.join([elem[::-1] for elem in stk])
