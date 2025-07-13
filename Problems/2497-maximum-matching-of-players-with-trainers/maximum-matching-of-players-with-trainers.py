class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p,t = len(players) ,len(trainers)
        players.sort()
        trainers.sort()
        c = 0
        for i in trainers:
            if c<p and players[c]<=i:
                c+= 1
        return c