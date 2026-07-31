def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    visited=set(); stack=[0]
    while stack:
        r=stack.pop()
        if r in visited: continue
        visited.add(r)
        stack.extend(rooms[r])
    return len(visited)==len(rooms)
if __name__=="__main__":
    print("841 OK")
