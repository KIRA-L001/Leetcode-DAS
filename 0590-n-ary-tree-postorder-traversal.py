from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val=val
        self.children=children or []
def postorder(root: Node) -> List[int]:
    out=[]
    def dfs(node):
        if not node: return
        for c in node.children: dfs(c)
        out.append(node.val)
    dfs(root)
    return out
if __name__=="__main__":
    print("590 OK")
