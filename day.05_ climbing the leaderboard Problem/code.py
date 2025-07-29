# this is a simple way of solving the problem of climbing the leaderboard
# using a simple list and sorting it in descending order
# it modifies the original ranked list by appending the player's score
# and then finding the rank of each player's score
## it is not the most efficient way, as it sorts the list multiple times

def climbingLeaderboard0(ranked, player):
    player_rank=[]
    for x in player:
        ranked.append(x)
        ranked = sorted(set(ranked), reverse=True)
        player_rank.append(ranked.index(x) + 1)
        ranked.pop(ranked.index(x))
        
    return   player_rank  

# this function uses a more efficient way of solving the problem
# by using a set to remove duplicates and then sorting the unique ranks
# it then iterates through the player's scores and finds their rank
# without modifying the original ranked list

def climbingLeaderboard1(ranked, player):
    unique_ranks = sorted(set(ranked), reverse=True)    
    results = []
    index = len(unique_ranks) - 1 
    for score in player:
        while index >= 0 and score >= unique_ranks[index]:
            index -= 1
        results.append(index + 2)
    
    return results    
# Example usage
print(climbingLeaderboard0([100,100,50,40,40,20,10], [5,25,50,120]))  # Output: [6, 4, 2, 1]
