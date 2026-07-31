def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans=[0]*len(temperatures)
    stack=[]
    for i,t in enumerate(temperatures):
        while stack and t>temperatures[stack[-1]]:
            prev=stack.pop()
            ans[prev]=i-prev
        stack.append(i)
    return ans
if __name__=="__main__":
    print("739 OK")
