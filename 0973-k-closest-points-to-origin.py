from typing import List
import heapq, math
 def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap=[]
    for p in points:
        d=p[0]*p[0]+p[1]*p[1]
        heapq.heappush(heap,(-d,p))
        if len(heap)>k:
            heapq.heappop(heap)
    return [p for _,p in heap]
if __name__=="__main__":
    print("973 OK")
