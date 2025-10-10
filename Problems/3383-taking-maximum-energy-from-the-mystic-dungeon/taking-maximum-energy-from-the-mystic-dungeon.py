class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for ind,v in enumerate(energy):
            if ind>=k:
                energy[ind]= max(v,v+energy[ind-k])
                energy[ind-k] = 0
        return max(energy[-k:])
            