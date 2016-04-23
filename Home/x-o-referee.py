#  Input: A game result as a list of strings (unicode).
#  Output: "X", "O" or "D" as a string. 

def checkio(game_result):
    horiz1 = game_result[0]
    horiz2 = game_result[1]
    horiz3 = game_result[2]
    vert1 = [row[0] for row in game_result]
    vert1 = (''.join(vert1))
    vert2 = [row[1] for row in game_result]
    vert2 = (''.join(vert2))
    vert3 = [row[2] for row in game_result]
    vert3 = (''.join(vert3))
    diag1 = game_result[0][0] + game_result[1][1] + game_result[2][2]
    diag2 = game_result[0][2] + game_result[1][1] + game_result[2][0]
    result = [horiz1, horiz2, horiz3, vert1, vert2, vert3, diag1, diag2]
    for x in result:
        if x == "XXX":
            return "X"
            
        if x == "OOO":
            return "O"
            
    return "D"
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

