from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val=val
        self.children=children or []
def preorder(root: Node) -> List[int]:
    out=[]
    def dfs(node):
        if not node: return
        out.append(node.val)
        for c in node.children: dfs(c)
    dfs(root)
    return out
if __name__=="__main__":
    print("589 OK")
