#  Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.
#  Output: Are these drones related or not as a boolean. 

def check_connection(network, first, second):
    future =[]
    visited = [first]
    conection = {}
    for x in network:
        x1, x2 = x.split('-')
        conection.setdefault(x1, []).append(x2)
        conection.setdefault(x2, []).append(x1)
    future = []
    while len(visited):
        now = visited.pop()
        future.append(now)
        if now == second:
            return True
        for next in conection.setdefault(now, []):
            if next not in future and next not in visited:
                visited.append(next)
    return False
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
