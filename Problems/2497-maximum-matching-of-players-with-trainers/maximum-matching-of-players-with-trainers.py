class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p,t = len(players) ,len(trainers)
        players.sort(reverse = True)
        trainers.sort(reverse = True)
        i,j= 0,0
        ans = 0
        while i<p and j<t:
            if players[i]<=trainers[j]:
                ans += 1
                i += 1
                j += 1

            else:
                i += 1
        
        return ans