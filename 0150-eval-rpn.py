from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in '+-*/':
                b, a = st.pop(), st.pop()
                st.append(a+b if t=='+' else a-b if t=='-' else a*b if t=='*' else int(a/b))
            else: st.append(int(t))
        return st[0]

# refreshed 20260821-102507
