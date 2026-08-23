# SQL: SELECT p.firstName, p.lastName, a.city, a.state
# FROM Person p LEFT JOIN Address a ON p.personId = a.personId
class Solution:
    def combineTwoTables(self, person: list, address: list) -> list:
        m = {a["personId"]: a for a in address}
        return [{"firstName": p["firstName"], "lastName": p["lastName"],
                 "city": m.get(p["personId"], {}).get("city"),
                 "state": m.get(p["personId"], {}).get("state")} for p in person]

# refreshed 20260823-123438
